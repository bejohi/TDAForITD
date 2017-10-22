from os import listdir
import sys
import morphdetect.loging as log
import traceback

from morphdetect.morph_skeleton import create_morph_skeleton, count_morph_relevant_pattern

image_report_path = "image_scan_result.txt"


def __get_all_image_paths_from_file_path(folder_path: str):
    """Searches for all pictures which are directly located in a given folder path and returns their path names in a
    list """
    image_list = []
    for file_name in listdir(folder_path):
        if file_name.endswith(".png") or file_name.endswith(".jpg"):
            image_path = folder_path + "\\" + file_name
            image_list.append(image_path)
    return image_list


def __process_cmd_line_parameter_and_create_image_path_list():
    """Reads the image folder path from the cmd lind and creates a list of all paths from included images.
    Exits the current process, if no cmd-line parameter was passed as path."""
    if len(sys.argv) != 2:
        print("You need to specify a folder path as first and only cmd parameter.")
        exit(-1)
    image_folder_path = str(sys.argv[1])
    log.log_info("Searching for images in path: " + image_folder_path)
    all_image_paths = __get_all_image_paths_from_file_path(image_folder_path)
    log.log_info(str(len(all_image_paths)) + " images where found.")
    return all_image_paths


def __process_morph_check(path: str):
    """Processes the build of a binary skeleton for a image behind the given image path. The function counts the
    morph relevant pixel number and stores the result on the hard drive. """
    morph_skeleton = create_morph_skeleton(path)
    count_morph_pattern = count_morph_relevant_pattern(morph_skeleton)
    morph_pattern_difference = len(morph_skeleton) * len(morph_skeleton[0]) - count_morph_pattern
    report_file = open(image_report_path, "a")
    report_string = str(path) + ";" + str(count_morph_pattern) + ";" + str(morph_pattern_difference)
    log.log_info(report_string)
    report_file.write(report_string + "\n")
    report_file.close()


if __name__ == "__main__":
    image_paths = __process_cmd_line_parameter_and_create_image_path_list()
    try:
        for im_path in image_paths:
            __process_morph_check(im_path)
    except:
        log.log_error(str(traceback.format_exc()))
        exit(-2)
