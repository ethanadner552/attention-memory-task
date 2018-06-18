

# This experiment was created by Kirsten Ziman (Kirsten.K.Ziman.gr@Dartmouth.edu)
# for more information, visit: www.context-lab.com


# Imports ############################################################################################

import psychopy
import sys
import pandas as pd
from psychopy import visual, event, core, data, gui, logging
#import pylinkwrapper
sys.path.insert(0, '../analysis/')
from analysis_helpers import *
from experiment_helpers import *
import time



# Set Up #############################################################################################

# Parameters #
experiment_title = 'Attention and Memory' 
practice = True   # instructions & practice
test_mode = False # not for use with subjects
save_data = True  # saves all data
eye_track = False # for eye tracking
MRI = False       # for MRI sync

params = {'runs':8, 'presentations_per_run':10, 'invalid_cue_percentage':10, 'mem_to_pres':4, 'mem_pres_split':2}
categories = {'cat1':'Faces', 'cat2':'Places', 'composites':'composites'}
paths = {'data_path':'../../data/', 'stim_path':'../../stim/'}

# Obtain participant info (pop-up) and make subdir #
info = subject_info(experiment_title, paths['data_path'])
subject_directory = subject_directory(info, paths['data_path'], path_only=True)

# Initiate clock #
global_clock = core.Clock()
logging.setDefaultClock(global_clock)

# pre questionnaire #
pre_info = pre_questionnaire(info, save=save_data, save_path=subject_directory)

# Window and Stimulus timing #
win = visual.Window([1024,768], fullscr = True, monitor = 'testMonitor', units='deg', color = 'black')
rate = win.getActualFrameRate()
timing = {'cue':int(round(1.5 * rate)), 'probe':int(round(3.0 * rate)), 'mem':int(round(2 * rate)), 'pause':int(round(1 *rate))}



# Run Experiment #####################################################################################




# Initiate log file #
# log_data = logging.LogFile(paths['data_path'] + subject_info['participant'] + '.log', filemode='w', level=logging.DATA)


# Window #



# Instructions & Practice #
#if practice:
    # run intro & pract rounds


# eye tracker callibration #
# if eye_track:
    
    
# MRI sync #
# if MRI:


# Initialize subject dataframe #
df = initialize_df(info, categories, paths, subject_directory, params) 

# create df masks
mask1 = df['Trial Type']=='Presentation'
mask2 = df['Trial Type']=='Memory'

# Pres & Mem runs #
for run in range(params['runs']):
    
    # show pres instruct (0 or other) 
    
    mask3 = df['Run']==run
    presentation_run(win, df.loc[mask1][mask3], params, timing, paths) 
    
    # show memory instruct (0 or other)
    
    memory_run(win, df.loc[mask2][mask3], params, timing, paths)
    

# post questionnaire #
#post_info = post_questionnaire(subject[0], save=save_data, save_path=paths['data_path'])

