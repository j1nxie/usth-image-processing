import sys

import image_processing

if __name__ == "__main__":
    try:
        image_processing.main()
    except KeyboardInterrupt:
        sys.exit(0)
