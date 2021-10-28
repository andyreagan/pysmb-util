import logging
import os

from smb.SMBConnection import SMBConnection

DATA_ROOT = "."

log_fmt = "[%(asctime)s - %(levelname)s] - %(name)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__file__)


class SMB(SMBConnection):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sock = None

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


def get_file_list(smb_creds: dict, path: str, pattern: str, service_name: str, dns: str) -> list:
    with SMB(**smb_creds) as conn:
        conn.connect(dns, timeout=5)
        fnames = conn.listPath(service_name=service_name, path=path, pattern=pattern)
    return fnames


def attach_file_stream(smb_creds: dict, path: str, file, stream, service_name: str, dns: str) -> None:
    with SMB(**smb_creds) as conn:
        conn.connect(dns, timeout=5)
        # with open(os.path.join(DATA_ROOT, file.filename), 'wb') as stream:
        if file.file_size > 0:
            _, fsize = conn.retrieveFile(
                service_name, "{path}/{fname}".format(path=path, fname=file.filename), stream
            )
            logger.info(
                "{file} was successfully copied via SMB and is {bytes_} bytes long".format(
                    file=file.filename, bytes_=fsize
                )
            )
        else:
            logger.info(
                "{file} is empty, consider removing it".format(file=file.filename)
            )
        # logger.info('deleting {file}'.format(file=file.filename))
        # conn.deleteFiles(service_name=service_name, path_file_pattern=file.filename)


def write_to_local_file(smb_creds: dict, path, file, service_name: str, dns: str):
    with open(os.path.join(DATA_ROOT, file.filename), "wb") as stream:
        attach_file_stream(smb_creds, path, file, stream, service_name, dns)
