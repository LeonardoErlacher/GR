import wfdb
import os

def try_reading_ecg():
    # To load a wfdb formatted ECG record
    hea_path = "/Users/vet/Documents/Uni Allgemein/Master/SS23/Guided Research/Daten/motion-artifact-contaminated-ecg-database-1.0.0/test20_45j"
    record = wfdb.rdrecord(hea_path)
    print(record)
    wfdb.plot_wfdb(record, title='Record a01 from Physionet Apnea ECG')

    folder_path= "/Users/vet/Documents/Uni Allgemein/Master/SS23/Guided Research/Daten/motion-artifact-contaminated-ecg-database-1.0.0/"
    for file in os.listdir(folder_path):
        if file.endswith(".hea"):
            print(file)
            file = file[:-4]
            print(file)
            record = wfdb.rdrecord(file)
            print(record)
            wfdb.plot_wfdb(record, title='Record a01 from Physionet Apnea ECG')



if __name__ == "__main__":
    try_reading_ecg()

