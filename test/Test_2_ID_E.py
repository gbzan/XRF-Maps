
#Don't forget to append XRF-Maps/bin directory to PYTHONPATH

import pyxrfmaps as px

element_csv_filename = "../reference/xrf_library.csv"
element_henke_filename = "../reference/henke.xdr"

if __name__ == '__main__':
    px.load_element_info(element_henke_filename, element_csv_filename)
    job = px.AnalysisJob()
    job.dataset_directory = '2_ID_E_dataset/'
    job.dataset_files = px.find_all_dataset_files(job.dataset_directory + "mda/", ".mda")
    job.optimize_dataset_files = job.dataset_files
    job.detector_num_start = 0
    job.detector_num_end = 3
    job.quick_and_dirty = False
    job.fitting_routines = [px.FittingRoutines.ROI, px.FittingRoutines.SVD, px.FittingRoutines.MATRIX, px.FittingRoutines.NNLS]
    job.quantification_standard_filename = 'maps_standardinfo.txt'
    px.check_and_create_dirs(job.dataset_directory)
    px.populate_netcdf_hdf5_files(job.dataset_directory)
    px.init_analysis_job_detectors(job)
    px.generate_optimal_params(job)
    px.perform_quantification(job)
    px.process_dataset_files(job)
    print('done')
