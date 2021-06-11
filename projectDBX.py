import dropbox
from dropbox.files import WriteMode
import os


class TransferData(object):
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFiles(self, file_from, file_to):
        # parameter should contain only access tokens
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            # 
            for filename in files:
                local_path = os.path.join(root, filename)
            # relative_path = os.path.relpath(file_from, dirs)
            #     dropbox_path = os.path.join(file_to, relative_path)

            # with open(file_from, 'rb')as f:
            #      # rb= read binary becos files r stored as bits
            #      # dbx.files_upload over here files_upload is predefined
            #      dbx.files_upload(f.read(), local_path)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
                print(relative_path)
                print(dropbox_path)

def main():
    access_token = "BNNbaXaRzCkAAAAAAAAAAcjVhkfDg7cRfG5YCWQ7OfU2mrrjIOzgqf_QmAxp2wcJ"
    transferData = TransferData(access_token)

    file_from = "/D:/Test"
    file_to = "/Dropbox/Test"

    transferData.uploadFiles(file_from, file_to)


main()
