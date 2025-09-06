import os
import mimetypes
from pathlib import Path


def entry_point(custom_path: str) -> None:
    verify_dir_existence(custom_path)


def verify_dir_existence(custom_path: str = None) -> None:
    user_home, path = "", ""
    if not custom_path:
        user_home = os.getenv('HOME')
        path: Path = Path(f'{user_home}')
    else:
        user_home = os.getenv('HOME')
        path: Path = Path(f'{user_home}/{custom_path}')

    PATH_TO_IMAGES: str = f'{path}/images'
    PATH_TO_PDFS: str = f'{path}/pdfs'
    PATH_TO_TEXTS: str = f'{path}/texts'

    try:
        os.makedirs(PATH_TO_IMAGES)
        os.makedirs(PATH_TO_PDFS)
        os.makedirs(PATH_TO_TEXTS)

        print("Directories created. (images, pdfs and texts...)")
    except OSError:
        print("Directories already created")
    finally:
        filter_dirs(path, PATH_TO_IMAGES, PATH_TO_PDFS, PATH_TO_TEXTS)


def filter_dirs(path: Path, img_path: str, pdf_path: str, text_path: str) -> None:
    imgs: set = set()
    txts: set = set()
    pdfs: set = set()

    for file in path.iterdir():
        try:
            # type = filetype.guess(str(file))
            file_converted: str = str(file)
            file_converted = mimetypes.guess_type(file_converted)

            if file_converted[0] in ["image/png", "image/jpeg", "image/gif"]:
                imgs.add(file)
                continue

            if file_converted[0] in ["application/pdf"]:
                pdfs.add(file)
                continue

            if file_converted[0] in ["text/plain"]:
                txts.add(file)
                continue
        except (TypeError, IsADirectoryError):
            continue

    move_files_to_dirs(path, img_path, pdf_path, text_path, imgs, txts, pdfs)


def move_files_to_dirs(path: Path, img_path: str, pdf_path: str, text_path: str,
                       img_set: set, txt_set: set, pdfs_set: set) -> bool:
    if img_set:
        for image in img_set:
            os.system(f'mv {str(image)} {img_path}')
        print("Images Were Organized.")
    else:
        print(f"No images on {path}")

    if pdfs_set:
        for pdf_current in pdfs_set:
            os.system(f'mv {str(pdf_current)} {pdf_path}')
        print("PDF's Were Organized.")
    else:
        print(f"No pdfs on {path}")

    if txt_set:
        for txt_current in txt_set:
            os.system(f'mv {str(txt_current)} {text_path}')
        print("Texts Were Organized.")
    else:
        print(f"No txts on {path}")

    return True
