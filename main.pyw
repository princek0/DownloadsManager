import os
import shutil
import getpass
import time
import watchdog

# File extension tuples.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
images = (
    ".png", ".jpg", ".gif", ".webp", ".tiff", ".psd", ".raw", ".bmp", ".heif", ".indd", ".svg", ".ai", ".eps", ".tif",
    ".PNG", ".JPG", ".GIF", ".WEBP", ".TIFF", ".PSD", ".RAW", ".BMP", ".HEIF", ".INDD", ".SVG", ".AI", ".EPS", ".TIF"
)

videos = (
    ".webm", ".mkv", ".flv", ".vob", ".ogv", ".ogg", ".drc", ".gifv", ".mng", ".avi", ".MTS", ".M2TS", ".TS", ".mov",
    ".qt",
    ".wmv", ".yuv", ".rm", "rmvb", ".viv", ".asf", ".amv", ".mp4", ".m4p", ".m4v", ".mpg", ".mp2", ".mpeg", ".mpe",
    ".mpv",
    ".m2v", ".m4v", ".svi", ".3gp", ".3g2", ".mxf", ".roq", ".nsv", ".flv", ".f4v", ".f4p", ".f4a", ".f4b", ".WEBM",
    ".MKV",
    ".FLV", ".VOB", ".OGV", ".OGG", ".DRC", ".GIFV", ".MNG", ".AVI", ".MTS", ".M2TS", ".TS", ".MOV", ".QT", ".WMV",
    ".YUV",
    ".RM", "RMVB", ".VIV", ".ASF", ".AMV", ".MP4", ".M4P", ".M4V", ".MPG", ".MP2", ".MPEG", ".MPE", ".MPV", ".M2V",
    ".M4V",
    ".SVI", ".3GP", ".3G2", ".MXF", ".ROQ", ".NSV", ".FLV", ".F4V", ".F4P", ".F4A", ".F4B"
)

texts = (".txt", ".pdf", ".rtf", ".odt", ".tex", ".wpd", ".TXT", ".PDF", ".RTF", ".ODT", ".TEX", ".WPD", ".PDF")

office365 = (
    ".doc", ".docx", ".pptx", ".pptm", ".ppt", ".xls", ".xlsb", ".xlsm", ".xlsx", ".DOC", ".DOCX", ".PPTX", ".PPTM",
    ".PPT",
    ".XLS", ".XLSB", ".XLSM", ".XLSX"
)

special = (
    ".exe", ".py", ".css", ".jar", ".xml", ".c", ".cgi", ".class", ".cpp", ".cs", ".h", ".java", ".php", ".csv", ".dat",
    ".db", ".dbf", ".log", ".mdb", ".sav", ".sql", ".tar", ".apk", ".bat", ".bin", ".pl", ".com", ".gadget", ".msi",
    ".wsf",
    ".asp", ".aspx", ".cer", ".cfm", ".css", ".htm", ".html", ".jsp", ".part", ".rss", ".xhtml", ".sh", ".swift", ".vb",
    ".bak", ".cab", ".cfg", ".cpl", ".cur", ".dll", ".dmp", ".drv", ".icns", ".ico", ".ini", ".ink", ".msi", ".sys",
    ".EXE", ".PY", ".CSS", ".JAR", ".XML", ".C", ".CGI", ".CLASS", ".CPP", ".CS", ".H", ".JAVA", ".PHP", ".CSV", ".DAT",
    ".DB", ".DBF", ".LOG", ".MDB", ".SAV", ".SQL", ".TAR", ".APK", ".BAT", ".BIN", ".PL", ".COM", ".GADGET", ".MSI",
    ".WSF",
    ".ASP", ".ASPX", ".CER", ".CFM", ".CSS", ".HTM", ".HTML", ".JSP", ".PART", ".RSS", ".XHTML", ".SH", ".SWIFT", ".VB",
    ".BAK", ".CAB", ".CFG", ".CPL", ".CUR", ".DLL", ".DMP", ".DRV", ".ICNS", ".ICO", ".INI", ".INK", ".MSI", ".SYS",
    ".js", ".JS"
)

incomplete = (".crdownload", ".tmp", ".CRDOWNLOAD", ".TMP")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Finds username of user on the PC.
homedir = os.path.expanduser("~")
USER_NAME = getpass.getuser()


# Adds program to start-up folder.
def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)


add_to_startup(__file__)

# Checks if folders exist, if not it creates them.
if not os.path.exists(homedir + r"/Downloads/Texts"):
    os.makedirs(homedir + r"/Downloads/Texts")
if not os.path.exists(homedir + r"/Downloads/Videos"):
    os.makedirs(homedir + r"/Downloads/Videos")
if not os.path.exists(homedir + r"/Downloads/Other"):
    os.makedirs(homedir + r"/Downloads/Other")
if not os.path.exists(homedir + r"/Downloads/Special"):
    os.makedirs(homedir + r"/Downloads/Special")
if not os.path.exists(homedir + r"/Downloads/Office365"):
    os.makedirs(homedir + r"/Downloads/Office365")
if not os.path.exists(homedir + r"/Downloads/Images"):
    os.makedirs(homedir + r"/Downloads/Images")

while True:
    time.sleep(600)
    try:
        # Moves images.
        for file in os.listdir(homedir + r"/Downloads"):
            if file.endswith(images):
                print(homedir + r"/Downloads/" + file)
                shutil.move(homedir + r"/Downloads/" + file, homedir + r"/Downloads/Images/" + file)

        # Moves videos.
        for file in os.listdir(homedir + r"/Downloads"):
            if file.endswith(videos):
                print(homedir + r"/Downloads/" + file)
                shutil.move(homedir + r"/Downloads/" + file, homedir + r"/Downloads/Videos/" + file)

        # Moves special files such as executables.
        for file in os.listdir(homedir + r"/Downloads"):
            if file.endswith(special):
                print(homedir + r"/Downloads/" + file)
                shutil.move(homedir + r"/Downloads/" + file,
                            homedir + r"/Downloads/Special/" + file)

        # Moves office365 files such as powerpoint files.
        for file in os.listdir(homedir + r"/Downloads"):
            if file.endswith(office365):
                print(r"C:/Users/User/Downloads/" + file)
                shutil.move(homedir + r"/Downloads/" + file,
                            homedir + r"/Downloads/Office365/" + file)

        # Moves text files such as pdfs.
        for file in os.listdir(homedir + r"/Downloads"):
            if file.endswith(texts):
                print(homedir + r"/Downloads/" + file)
                shutil.move(homedir + r"/Downloads/" + file, homedir + r"/Downloads/Texts/" + file)

        # Moves everything that doesn't fit into the other categories.
        for file in os.listdir(homedir + r"/Downloads"):
            if os.path.isfile(homedir + r"/Downloads/" + file):
                if not file.endswith(texts) and not file.endswith(office365) and not file.endswith(
                        special) and not file.endswith(videos) and not file.endswith(images) and not file.endswith(
                    incomplete):
                    print(file)
                    print(homedir + r"/Downloads/" + file)
                    shutil.move(homedir + r"/Downloads/" + file, homedir + r"/Downloads/Other/" + file)
    except:
        print("An error occurred.")
