# import logging để tạo logger
import logging

# import os để xử lý folder/file path
import os


# tạo folder logs nếu folder này chưa tồn tại
os.makedirs("logs", exist_ok=True)


# hàm tạo logger dùng chung cho framework
def get_logger(name):

    # tạo logger theo tên module truyền vào
    logger = logging.getLogger(name)

    # set mức log thấp nhất là INFO
    logger.setLevel(logging.INFO)

    # nếu logger đã có handler thì return luôn để tránh log bị duplicate
    if logger.handlers:

        # return logger hiện tại
        return logger

    # tạo format cho log message
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    # tạo handler ghi log ra file
    file_handler = logging.FileHandler("logs/automation.log", encoding="utf-8")

    # set format cho file handler
    file_handler.setFormatter(formatter)

    # tạo handler hiển thị log ra console
    console_handler = logging.StreamHandler()

    # set format cho console handler
    console_handler.setFormatter(formatter)

    # add file handler vào logger
    logger.addHandler(file_handler)

    # add console handler vào logger
    logger.addHandler(console_handler)

    # return logger để file khác sử dụng
    return logger