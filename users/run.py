# pylint: skip-file
import uvicorn
import sys
print("sssssssssss")
if __name__ == "__main__":
    # freeze_support()
    sys.argv.insert(1, "manage:app")
    sys.exit(uvicorn.main())
