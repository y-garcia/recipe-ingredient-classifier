import sagemaker
import boto3
import os
import shutil
import sys
import threading

class S3Util:
    def __init__(self, s3_folder='capstone-project', data_directory='data', model_directory='model'):
        self.session = sagemaker.Session()
        self.bucket_name = self.session.default_bucket()
        self.S3 = boto3.client('s3')
        self.bucket = boto3.Session().resource('s3').Bucket(self.bucket_name)
        self.s3_folder = s3_folder
        self.data_directory = data_directory
        self.model_directory = model_directory
        
    def save_data_to_s3(self):
        for entry in os.scandir(self.data_directory):
            local_file =  os.path.join(self.data_directory, entry.name)
            s3_file = os.path.join(self.s3_folder, local_file)
            self.bucket.Object(s3_file).upload_file(local_file)
            os.remove(local_file)
            
    def save_models_to_s3(self):
        for entry in os.scandir(self.model_directory):
            if(entry.is_dir()):
                print(f'Zipping {entry.path} ...')
                shutil.make_archive(entry.path, 'zip', self.model_directory)
                zip_file = f'{os.path.join(self.model_directory, entry.name)}.zip'
                s3_file = os.path.join(self.s3_folder, zip_file)
                print(f'Uploading {zip_file} to {s3_file} ...')
                self.bucket.Object(s3_file).upload_file(zip_file)
                print(f'Removing {zip_file} ...')
                os.remove(zip_file)
                print(f'Removing {entry.path} ...')
                shutil.rmtree(entry.path)
                
    def get_data_from_s3(self, filenames):
        for filename in filenames:
            s3_file = os.path.join(self.s3_folder, self.data_directory, filename)
            local_file = os.path.join(self.data_directory, filename)
            print(f'Downloading {s3_file} to {local_file} ...')
            self.S3.download_file(self.bucket_name, s3_file, local_file)
    
    def get_model_from_s3(self, model_name):
        s3_file = f'{os.path.join(self.s3_folder, self.model_directory, model_name)}.zip'
        zip_file = f'{os.path.join(self.model_directory, model_name)}.zip'
        print(f'Downloading model {s3_file} to {zip_file} ...')
        file_size = self.S3.head_object(Bucket=self.bucket_name, Key=s3_file)['ContentLength']
        self.S3.download_file(self.bucket_name, s3_file, zip_file, Callback=ProgressPercentage(zip_file, self.model_directory, file_size))
        
    def unpack(self, model_name):
        zip_file = f'{os.path.join(self.model_directory, model_name)}.zip'
        print(f'Unzipping {zip_file} ...')
        shutil.unpack_archive(zip_file, self.model_directory)
        print(f'Removing {zip_file} ...')
        os.remove(zip_file)


class ProgressPercentage(object):

    def __init__(self, filename, directory, file_size):
        self._filename = filename
        self._directory = directory
        self._size = file_size
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()
            
    def unzip(self, zip_file, directory):
        print(f'Unzipping {zip_file} ...')
        shutil.unpack_archive(zip_file, directory)
        print(f'Removing {zip_file} ...')
        os.remove(zip_file)