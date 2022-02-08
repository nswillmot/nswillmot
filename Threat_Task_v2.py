#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Tue Feb  8 15:51:07 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('latest')


from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'sounddevice'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'ThreatTask'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/macbook/Google Drive/UQ/Military Study/Nick_UQ HPRnet Stimuli/PsychoPy/Threat_Task_v2.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Setup"
SetupClock = core.Clock()
import random
# Randomly choose a response mapping condition for each participant
Condition = random.choice(('A', 'B', 'C', 'D'))
#Define baseline files
baseline_file1 = 'Baseline1_' + Condition + '_1.xlsx'
baseline_file2 = 'Baseline2_' + Condition + '_1.xlsx'
#Define Training files for tasks (Threat_Condition_KeyMap.xlsx)
training_file1 = 'Threat_' + Condition + '_1.xlsx'
training_file2 = 'Threat_' + Condition + '_2.xlsx'
training_file3 = 'Threat_' + Condition + '_3.xlsx'
training_file4 = 'Threat_' + Condition + '_4.xlsx'
#Define test files
Test_file1 = 'Test1_' + Condition + '_1xlsx'
Test_file2 = 'Test2_' + Condition + '_1xlsx'
#Hide the mouse
win.mouseVisible = False

# Initialize components for Routine "Task_Instructions"
Task_InstructionsClock = core.Clock()
Instructions_2 = visual.TextStim(win=win, name='Instructions_2',
    text='In this block you will be presented a series of images. Some of these images will have threats present.\n\nPress A if you sense a threat may be present. \n\nPress L for no threat\n\nRemember, please respond as QUICKLY and ACCURATELY as you can.\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
PAK_2 = visual.TextStim(win=win, name='PAK_2',
    text='Press any key to begin practice block',
    font='Open Sans',
    pos=(0, -0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "Threat_NoThreat"
Threat_NoThreatClock = core.Clock()
Fixation = visual.ShapeStim(
    win=win, name='Fixation', vertices='cross',units='height', 
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=0.0, interpolate=True)
Stim = visual.ImageStim(
    win=win,
    name='Stim', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
Response = keyboard.Keyboard()
Fixation2_2 = visual.ShapeStim(
    win=win, name='Fixation2_2', vertices='cross',units='height', 
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-3.0, interpolate=True)

# Initialize components for Routine "Threat_NoThreat"
Threat_NoThreatClock = core.Clock()
Fixation = visual.ShapeStim(
    win=win, name='Fixation', vertices='cross',units='height', 
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=0.0, interpolate=True)
Stim = visual.ImageStim(
    win=win,
    name='Stim', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
Response = keyboard.Keyboard()
Fixation2_2 = visual.ShapeStim(
    win=win, name='Fixation2_2', vertices='cross',units='height', 
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-3.0, interpolate=True)

# Initialize components for Routine "Threat_NoThreat"
Threat_NoThreatClock = core.Clock()
Fixation = visual.ShapeStim(
    win=win, name='Fixation', vertices='cross',units='height', 
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=0.0, interpolate=True)
Stim = visual.ImageStim(
    win=win,
    name='Stim', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
Response = keyboard.Keyboard()
Fixation2_2 = visual.ShapeStim(
    win=win, name='Fixation2_2', vertices='cross',units='height', 
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-3.0, interpolate=True)

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
Stimuli_1 = visual.ImageStim(
    win=win,
    name='Stimuli_1', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
#AudioCorr_Threat = sound.Sound(u'Threat_Correct.wav')
#AudioCorr_NoThreat = sound.Sound(u'NoThreat_Correct.wav')
#AudioIncorr_Threat = sound.Sound(u'Threat_Incorrect.wav')
#AudioIncorr_NoThreat = sound.Sound(u'NoThreat_Incorrect.wav')

AudCorr_ = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='AudCorr_')
AudCorr_.setVolume(1.0)
AudIncorr_ = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='AudIncorr_')
AudIncorr_.setVolume(1.0)
CorrImg = visual.ImageStim(
    win=win,
    name='CorrImg', units='norm', 
    image='CorrAns.png', mask=None,
    ori=0.0, pos=[0,0], size=(0.2,0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
IncorrImg = visual.ImageStim(
    win=win,
    name='IncorrImg', units='norm', 
    image='IncorrAns.png', mask=None,
    ori=0.0, pos=[0,0], size=(0.2,0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# Initialize components for Routine "Threat_NoThreat"
Threat_NoThreatClock = core.Clock()
Fixation = visual.ShapeStim(
    win=win, name='Fixation', vertices='cross',units='height', 
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=0.0, interpolate=True)
Stim = visual.ImageStim(
    win=win,
    name='Stim', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
Response = keyboard.Keyboard()
Fixation2_2 = visual.ShapeStim(
    win=win, name='Fixation2_2', vertices='cross',units='height', 
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-3.0, interpolate=True)

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
Stimuli_1 = visual.ImageStim(
    win=win,
    name='Stimuli_1', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
#AudioCorr_Threat = sound.Sound(u'Threat_Correct.wav')
#AudioCorr_NoThreat = sound.Sound(u'NoThreat_Correct.wav')
#AudioIncorr_Threat = sound.Sound(u'Threat_Incorrect.wav')
#AudioIncorr_NoThreat = sound.Sound(u'NoThreat_Incorrect.wav')

AudCorr_ = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='AudCorr_')
AudCorr_.setVolume(1.0)
AudIncorr_ = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='AudIncorr_')
AudIncorr_.setVolume(1.0)
CorrImg = visual.ImageStim(
    win=win,
    name='CorrImg', units='norm', 
    image='CorrAns.png', mask=None,
    ori=0.0, pos=[0,0], size=(0.2,0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
IncorrImg = visual.ImageStim(
    win=win,
    name='IncorrImg', units='norm', 
    image='IncorrAns.png', mask=None,
    ori=0.0, pos=[0,0], size=(0.2,0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# Initialize components for Routine "Threat_NoThreat"
Threat_NoThreatClock = core.Clock()
Fixation = visual.ShapeStim(
    win=win, name='Fixation', vertices='cross',units='height', 
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=0.0, interpolate=True)
Stim = visual.ImageStim(
    win=win,
    name='Stim', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
Response = keyboard.Keyboard()
Fixation2_2 = visual.ShapeStim(
    win=win, name='Fixation2_2', vertices='cross',units='height', 
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-3.0, interpolate=True)

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
Stimuli_1 = visual.ImageStim(
    win=win,
    name='Stimuli_1', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
#AudioCorr_Threat = sound.Sound(u'Threat_Correct.wav')
#AudioCorr_NoThreat = sound.Sound(u'NoThreat_Correct.wav')
#AudioIncorr_Threat = sound.Sound(u'Threat_Incorrect.wav')
#AudioIncorr_NoThreat = sound.Sound(u'NoThreat_Incorrect.wav')

AudCorr_ = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='AudCorr_')
AudCorr_.setVolume(1.0)
AudIncorr_ = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='AudIncorr_')
AudIncorr_.setVolume(1.0)
CorrImg = visual.ImageStim(
    win=win,
    name='CorrImg', units='norm', 
    image='CorrAns.png', mask=None,
    ori=0.0, pos=[0,0], size=(0.2,0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
IncorrImg = visual.ImageStim(
    win=win,
    name='IncorrImg', units='norm', 
    image='IncorrAns.png', mask=None,
    ori=0.0, pos=[0,0], size=(0.2,0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# Initialize components for Routine "Threat_NoThreat"
Threat_NoThreatClock = core.Clock()
Fixation = visual.ShapeStim(
    win=win, name='Fixation', vertices='cross',units='height', 
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=0.0, interpolate=True)
Stim = visual.ImageStim(
    win=win,
    name='Stim', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
Response = keyboard.Keyboard()
Fixation2_2 = visual.ShapeStim(
    win=win, name='Fixation2_2', vertices='cross',units='height', 
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-3.0, interpolate=True)

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
Stimuli_1 = visual.ImageStim(
    win=win,
    name='Stimuli_1', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
#AudioCorr_Threat = sound.Sound(u'Threat_Correct.wav')
#AudioCorr_NoThreat = sound.Sound(u'NoThreat_Correct.wav')
#AudioIncorr_Threat = sound.Sound(u'Threat_Incorrect.wav')
#AudioIncorr_NoThreat = sound.Sound(u'NoThreat_Incorrect.wav')

AudCorr_ = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='AudCorr_')
AudCorr_.setVolume(1.0)
AudIncorr_ = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='AudIncorr_')
AudIncorr_.setVolume(1.0)
CorrImg = visual.ImageStim(
    win=win,
    name='CorrImg', units='norm', 
    image='CorrAns.png', mask=None,
    ori=0.0, pos=[0,0], size=(0.2,0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
IncorrImg = visual.ImageStim(
    win=win,
    name='IncorrImg', units='norm', 
    image='IncorrAns.png', mask=None,
    ori=0.0, pos=[0,0], size=(0.2,0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# Initialize components for Routine "Threat_NoThreat"
Threat_NoThreatClock = core.Clock()
Fixation = visual.ShapeStim(
    win=win, name='Fixation', vertices='cross',units='height', 
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=0.0, interpolate=True)
Stim = visual.ImageStim(
    win=win,
    name='Stim', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
Response = keyboard.Keyboard()
Fixation2_2 = visual.ShapeStim(
    win=win, name='Fixation2_2', vertices='cross',units='height', 
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-3.0, interpolate=True)

# Initialize components for Routine "Threat_NoThreat"
Threat_NoThreatClock = core.Clock()
Fixation = visual.ShapeStim(
    win=win, name='Fixation', vertices='cross',units='height', 
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=0.0, interpolate=True)
Stim = visual.ImageStim(
    win=win,
    name='Stim', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
Response = keyboard.Keyboard()
Fixation2_2 = visual.ShapeStim(
    win=win, name='Fixation2_2', vertices='cross',units='height', 
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-3.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Setup"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
SetupComponents = []
for thisComponent in SetupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SetupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Setup"-------
while continueRoutine:
    # get current time
    t = SetupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SetupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SetupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Setup"-------
for thisComponent in SetupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Task_Instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
Task_InstructionsComponents = [Instructions_2, PAK_2, key_resp_6]
for thisComponent in Task_InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Task_InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Task_Instructions"-------
while continueRoutine:
    # get current time
    t = Task_InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Task_InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions_2* updates
    if Instructions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions_2.frameNStart = frameN  # exact frame index
        Instructions_2.tStart = t  # local t and not account for scr refresh
        Instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions_2, 'tStartRefresh')  # time at next scr refresh
        Instructions_2.setAutoDraw(True)
    
    # *PAK_2* updates
    if PAK_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PAK_2.frameNStart = frameN  # exact frame index
        PAK_2.tStart = t  # local t and not account for scr refresh
        PAK_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PAK_2, 'tStartRefresh')  # time at next scr refresh
        PAK_2.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=None, waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Task_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Task_Instructions"-------
for thisComponent in Task_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instructions_2.started', Instructions_2.tStartRefresh)
thisExp.addData('Instructions_2.stopped', Instructions_2.tStopRefresh)
thisExp.addData('PAK_2.started', PAK_2.tStartRefresh)
thisExp.addData('PAK_2.stopped', PAK_2.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
# the Routine "Task_Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Baseline1 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(baseline_file1),
    seed=None, name='Baseline1')
thisExp.addLoop(Baseline1)  # add the loop to the experiment
thisBaseline1 = Baseline1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBaseline1.rgb)
if thisBaseline1 != None:
    for paramName in thisBaseline1:
        exec('{} = thisBaseline1[paramName]'.format(paramName))

for thisBaseline1 in Baseline1:
    currentLoop = Baseline1
    # abbreviate parameter names if possible (e.g. rgb = thisBaseline1.rgb)
    if thisBaseline1 != None:
        for paramName in thisBaseline1:
            exec('{} = thisBaseline1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Threat_NoThreat"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    Stim.setImage(Stimuli)
    Response.keys = []
    Response.rt = []
    _Response_allKeys = []
    # keep track of which components have finished
    Threat_NoThreatComponents = [Fixation, Stim, Response, Fixation2_2]
    for thisComponent in Threat_NoThreatComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Threat_NoThreatClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Threat_NoThreat"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Threat_NoThreatClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Threat_NoThreatClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        if Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                Fixation.setAutoDraw(False)
        
        # *Stim* updates
        if Stim.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Stim.frameNStart = frameN  # exact frame index
            Stim.tStart = t  # local t and not account for scr refresh
            Stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
            Stim.setAutoDraw(True)
        if Stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Stim.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                Stim.tStop = t  # not accounting for scr refresh
                Stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Stim, 'tStopRefresh')  # time at next scr refresh
                Stim.setAutoDraw(False)
        
        # *Response* updates
        waitOnFlip = False
        if Response.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Response.frameNStart = frameN  # exact frame index
            Response.tStart = t  # local t and not account for scr refresh
            Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response, 'tStartRefresh')  # time at next scr refresh
            Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Response.clock.reset)  # t=0 on next screen flip
        if Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                Response.tStop = t  # not accounting for scr refresh
                Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Response, 'tStopRefresh')  # time at next scr refresh
                Response.status = FINISHED
        if Response.status == STARTED and not waitOnFlip:
            theseKeys = Response.getKeys(keyList=['a', 'l'], waitRelease=False)
            _Response_allKeys.extend(theseKeys)
            if len(_Response_allKeys):
                Response.keys = _Response_allKeys[-1].name  # just the last key pressed
                Response.rt = _Response_allKeys[-1].rt
                # was this correct?
                if (Response.keys == str(CorrectAns)) or (Response.keys == CorrectAns):
                    Response.corr = 1
                else:
                    Response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *Fixation2_2* updates
        if Fixation2_2.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation2_2.frameNStart = frameN  # exact frame index
            Fixation2_2.tStart = t  # local t and not account for scr refresh
            Fixation2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation2_2, 'tStartRefresh')  # time at next scr refresh
            Fixation2_2.setAutoDraw(True)
        if Fixation2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation2_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Fixation2_2.tStop = t  # not accounting for scr refresh
                Fixation2_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation2_2, 'tStopRefresh')  # time at next scr refresh
                Fixation2_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Threat_NoThreatComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Threat_NoThreat"-------
    for thisComponent in Threat_NoThreatComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Baseline1.addData('Fixation.started', Fixation.tStartRefresh)
    Baseline1.addData('Fixation.stopped', Fixation.tStopRefresh)
    Baseline1.addData('Stim.started', Stim.tStartRefresh)
    Baseline1.addData('Stim.stopped', Stim.tStopRefresh)
    # check responses
    if Response.keys in ['', [], None]:  # No response was made
        Response.keys = None
        # was no response the correct answer?!
        if str(CorrectAns).lower() == 'none':
           Response.corr = 1;  # correct non-response
        else:
           Response.corr = 0;  # failed to respond (incorrectly)
    # store data for Baseline1 (TrialHandler)
    Baseline1.addData('Response.keys',Response.keys)
    Baseline1.addData('Response.corr', Response.corr)
    if Response.keys != None:  # we had a response
        Baseline1.addData('Response.rt', Response.rt)
    Baseline1.addData('Response.started', Response.tStartRefresh)
    Baseline1.addData('Response.stopped', Response.tStopRefresh)
    Baseline1.addData('Fixation2_2.started', Fixation2_2.tStartRefresh)
    Baseline1.addData('Fixation2_2.stopped', Fixation2_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Baseline1'


# set up handler to look after randomisation of conditions etc
Baseline2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(baseline_file2),
    seed=None, name='Baseline2')
thisExp.addLoop(Baseline2)  # add the loop to the experiment
thisBaseline2 = Baseline2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBaseline2.rgb)
if thisBaseline2 != None:
    for paramName in thisBaseline2:
        exec('{} = thisBaseline2[paramName]'.format(paramName))

for thisBaseline2 in Baseline2:
    currentLoop = Baseline2
    # abbreviate parameter names if possible (e.g. rgb = thisBaseline2.rgb)
    if thisBaseline2 != None:
        for paramName in thisBaseline2:
            exec('{} = thisBaseline2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Threat_NoThreat"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    Stim.setImage(Stimuli)
    Response.keys = []
    Response.rt = []
    _Response_allKeys = []
    # keep track of which components have finished
    Threat_NoThreatComponents = [Fixation, Stim, Response, Fixation2_2]
    for thisComponent in Threat_NoThreatComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Threat_NoThreatClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Threat_NoThreat"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Threat_NoThreatClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Threat_NoThreatClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        if Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                Fixation.setAutoDraw(False)
        
        # *Stim* updates
        if Stim.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Stim.frameNStart = frameN  # exact frame index
            Stim.tStart = t  # local t and not account for scr refresh
            Stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
            Stim.setAutoDraw(True)
        if Stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Stim.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                Stim.tStop = t  # not accounting for scr refresh
                Stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Stim, 'tStopRefresh')  # time at next scr refresh
                Stim.setAutoDraw(False)
        
        # *Response* updates
        waitOnFlip = False
        if Response.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Response.frameNStart = frameN  # exact frame index
            Response.tStart = t  # local t and not account for scr refresh
            Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response, 'tStartRefresh')  # time at next scr refresh
            Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Response.clock.reset)  # t=0 on next screen flip
        if Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                Response.tStop = t  # not accounting for scr refresh
                Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Response, 'tStopRefresh')  # time at next scr refresh
                Response.status = FINISHED
        if Response.status == STARTED and not waitOnFlip:
            theseKeys = Response.getKeys(keyList=['a', 'l'], waitRelease=False)
            _Response_allKeys.extend(theseKeys)
            if len(_Response_allKeys):
                Response.keys = _Response_allKeys[-1].name  # just the last key pressed
                Response.rt = _Response_allKeys[-1].rt
                # was this correct?
                if (Response.keys == str(CorrectAns)) or (Response.keys == CorrectAns):
                    Response.corr = 1
                else:
                    Response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *Fixation2_2* updates
        if Fixation2_2.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation2_2.frameNStart = frameN  # exact frame index
            Fixation2_2.tStart = t  # local t and not account for scr refresh
            Fixation2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation2_2, 'tStartRefresh')  # time at next scr refresh
            Fixation2_2.setAutoDraw(True)
        if Fixation2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation2_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Fixation2_2.tStop = t  # not accounting for scr refresh
                Fixation2_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation2_2, 'tStopRefresh')  # time at next scr refresh
                Fixation2_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Threat_NoThreatComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Threat_NoThreat"-------
    for thisComponent in Threat_NoThreatComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Baseline2.addData('Fixation.started', Fixation.tStartRefresh)
    Baseline2.addData('Fixation.stopped', Fixation.tStopRefresh)
    Baseline2.addData('Stim.started', Stim.tStartRefresh)
    Baseline2.addData('Stim.stopped', Stim.tStopRefresh)
    # check responses
    if Response.keys in ['', [], None]:  # No response was made
        Response.keys = None
        # was no response the correct answer?!
        if str(CorrectAns).lower() == 'none':
           Response.corr = 1;  # correct non-response
        else:
           Response.corr = 0;  # failed to respond (incorrectly)
    # store data for Baseline2 (TrialHandler)
    Baseline2.addData('Response.keys',Response.keys)
    Baseline2.addData('Response.corr', Response.corr)
    if Response.keys != None:  # we had a response
        Baseline2.addData('Response.rt', Response.rt)
    Baseline2.addData('Response.started', Response.tStartRefresh)
    Baseline2.addData('Response.stopped', Response.tStopRefresh)
    Baseline2.addData('Fixation2_2.started', Fixation2_2.tStartRefresh)
    Baseline2.addData('Fixation2_2.stopped', Fixation2_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Baseline2'


# set up handler to look after randomisation of conditions etc
Training_Block1 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(training_file1),
    seed=None, name='Training_Block1')
thisExp.addLoop(Training_Block1)  # add the loop to the experiment
thisTraining_Block1 = Training_Block1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTraining_Block1.rgb)
if thisTraining_Block1 != None:
    for paramName in thisTraining_Block1:
        exec('{} = thisTraining_Block1[paramName]'.format(paramName))

for thisTraining_Block1 in Training_Block1:
    currentLoop = Training_Block1
    # abbreviate parameter names if possible (e.g. rgb = thisTraining_Block1.rgb)
    if thisTraining_Block1 != None:
        for paramName in thisTraining_Block1:
            exec('{} = thisTraining_Block1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Threat_NoThreat"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    Stim.setImage(Stimuli)
    Response.keys = []
    Response.rt = []
    _Response_allKeys = []
    # keep track of which components have finished
    Threat_NoThreatComponents = [Fixation, Stim, Response, Fixation2_2]
    for thisComponent in Threat_NoThreatComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Threat_NoThreatClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Threat_NoThreat"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Threat_NoThreatClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Threat_NoThreatClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        if Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                Fixation.setAutoDraw(False)
        
        # *Stim* updates
        if Stim.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Stim.frameNStart = frameN  # exact frame index
            Stim.tStart = t  # local t and not account for scr refresh
            Stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
            Stim.setAutoDraw(True)
        if Stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Stim.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                Stim.tStop = t  # not accounting for scr refresh
                Stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Stim, 'tStopRefresh')  # time at next scr refresh
                Stim.setAutoDraw(False)
        
        # *Response* updates
        waitOnFlip = False
        if Response.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Response.frameNStart = frameN  # exact frame index
            Response.tStart = t  # local t and not account for scr refresh
            Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response, 'tStartRefresh')  # time at next scr refresh
            Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Response.clock.reset)  # t=0 on next screen flip
        if Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                Response.tStop = t  # not accounting for scr refresh
                Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Response, 'tStopRefresh')  # time at next scr refresh
                Response.status = FINISHED
        if Response.status == STARTED and not waitOnFlip:
            theseKeys = Response.getKeys(keyList=['a', 'l'], waitRelease=False)
            _Response_allKeys.extend(theseKeys)
            if len(_Response_allKeys):
                Response.keys = _Response_allKeys[-1].name  # just the last key pressed
                Response.rt = _Response_allKeys[-1].rt
                # was this correct?
                if (Response.keys == str(CorrectAns)) or (Response.keys == CorrectAns):
                    Response.corr = 1
                else:
                    Response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *Fixation2_2* updates
        if Fixation2_2.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation2_2.frameNStart = frameN  # exact frame index
            Fixation2_2.tStart = t  # local t and not account for scr refresh
            Fixation2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation2_2, 'tStartRefresh')  # time at next scr refresh
            Fixation2_2.setAutoDraw(True)
        if Fixation2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation2_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Fixation2_2.tStop = t  # not accounting for scr refresh
                Fixation2_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation2_2, 'tStopRefresh')  # time at next scr refresh
                Fixation2_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Threat_NoThreatComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Threat_NoThreat"-------
    for thisComponent in Threat_NoThreatComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Training_Block1.addData('Fixation.started', Fixation.tStartRefresh)
    Training_Block1.addData('Fixation.stopped', Fixation.tStopRefresh)
    Training_Block1.addData('Stim.started', Stim.tStartRefresh)
    Training_Block1.addData('Stim.stopped', Stim.tStopRefresh)
    # check responses
    if Response.keys in ['', [], None]:  # No response was made
        Response.keys = None
        # was no response the correct answer?!
        if str(CorrectAns).lower() == 'none':
           Response.corr = 1;  # correct non-response
        else:
           Response.corr = 0;  # failed to respond (incorrectly)
    # store data for Training_Block1 (TrialHandler)
    Training_Block1.addData('Response.keys',Response.keys)
    Training_Block1.addData('Response.corr', Response.corr)
    if Response.keys != None:  # we had a response
        Training_Block1.addData('Response.rt', Response.rt)
    Training_Block1.addData('Response.started', Response.tStartRefresh)
    Training_Block1.addData('Response.stopped', Response.tStopRefresh)
    Training_Block1.addData('Fixation2_2.started', Fixation2_2.tStartRefresh)
    Training_Block1.addData('Fixation2_2.stopped', Fixation2_2.tStopRefresh)
    
    # ------Prepare to start Routine "Feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    Stimuli_1.setImage(Stimuli)
    #if Threat == 'Y' and Response.corr == True:
    #    AudioCorr_Threat.play()
    #elif Threat == 'Y' and Response.corr == False:
    #    AudioIncorr_Threat.play()
    #elif Threat == 'N' and Response.corr == True:
    #    AudioCorr_NoThreat.play()
    #    VisCorr_.opacity = 0.0
    #elif Threat == 'N' and Response.corr == False:
    #    AudioIncorr_NoThreat.play()
    #    VisIncorr_.opacity = 0.0
    AudCorr_.setSound(AudioCorr, secs=3, hamming=True)
    AudCorr_.setVolume(1.0, log=False)
    AudIncorr_.setSound(AudioIncorr, secs=3, hamming=True)
    AudIncorr_.setVolume(1.0, log=False)
    CorrImg.setOpacity(Opacity)
    CorrImg.setPos(Location)
    IncorrImg.setOpacity(Opacity)
    IncorrImg.setPos(Location)
    # keep track of which components have finished
    FeedbackComponents = [Stimuli_1, AudCorr_, AudIncorr_, CorrImg, IncorrImg]
    for thisComponent in FeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Feedback"-------
    while continueRoutine:
        # get current time
        t = FeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Stimuli_1* updates
        if Stimuli_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Stimuli_1.frameNStart = frameN  # exact frame index
            Stimuli_1.tStart = t  # local t and not account for scr refresh
            Stimuli_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stimuli_1, 'tStartRefresh')  # time at next scr refresh
            Stimuli_1.setAutoDraw(True)
        if Stimuli_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Stimuli_1.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                Stimuli_1.tStop = t  # not accounting for scr refresh
                Stimuli_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Stimuli_1, 'tStopRefresh')  # time at next scr refresh
                Stimuli_1.setAutoDraw(False)
        if t >= 5:
            continueRoutine = False
        # start/stop AudCorr_
        if AudCorr_.status == NOT_STARTED and Response.corr == True:
            # keep track of start time/frame for later
            AudCorr_.frameNStart = frameN  # exact frame index
            AudCorr_.tStart = t  # local t and not account for scr refresh
            AudCorr_.tStartRefresh = tThisFlipGlobal  # on global time
            AudCorr_.play(when=win)  # sync with win flip
        if AudCorr_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > AudCorr_.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                AudCorr_.tStop = t  # not accounting for scr refresh
                AudCorr_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(AudCorr_, 'tStopRefresh')  # time at next scr refresh
                AudCorr_.stop()
        # start/stop AudIncorr_
        if AudIncorr_.status == NOT_STARTED and Response.corr == False:
            # keep track of start time/frame for later
            AudIncorr_.frameNStart = frameN  # exact frame index
            AudIncorr_.tStart = t  # local t and not account for scr refresh
            AudIncorr_.tStartRefresh = tThisFlipGlobal  # on global time
            AudIncorr_.play(when=win)  # sync with win flip
        if AudIncorr_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > AudIncorr_.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                AudIncorr_.tStop = t  # not accounting for scr refresh
                AudIncorr_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(AudIncorr_, 'tStopRefresh')  # time at next scr refresh
                AudIncorr_.stop()
        
        # *CorrImg* updates
        if CorrImg.status == NOT_STARTED and Response.corr == True:
            # keep track of start time/frame for later
            CorrImg.frameNStart = frameN  # exact frame index
            CorrImg.tStart = t  # local t and not account for scr refresh
            CorrImg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CorrImg, 'tStartRefresh')  # time at next scr refresh
            CorrImg.setAutoDraw(True)
        if CorrImg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CorrImg.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                CorrImg.tStop = t  # not accounting for scr refresh
                CorrImg.frameNStop = frameN  # exact frame index
                win.timeOnFlip(CorrImg, 'tStopRefresh')  # time at next scr refresh
                CorrImg.setAutoDraw(False)
        
        # *IncorrImg* updates
        if IncorrImg.status == NOT_STARTED and Response.corr == False:
            # keep track of start time/frame for later
            IncorrImg.frameNStart = frameN  # exact frame index
            IncorrImg.tStart = t  # local t and not account for scr refresh
            IncorrImg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IncorrImg, 'tStartRefresh')  # time at next scr refresh
            IncorrImg.setAutoDraw(True)
        if IncorrImg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > IncorrImg.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                IncorrImg.tStop = t  # not accounting for scr refresh
                IncorrImg.frameNStop = frameN  # exact frame index
                win.timeOnFlip(IncorrImg, 'tStopRefresh')  # time at next scr refresh
                IncorrImg.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Training_Block1.addData('Stimuli_1.started', Stimuli_1.tStartRefresh)
    Training_Block1.addData('Stimuli_1.stopped', Stimuli_1.tStopRefresh)
    AudCorr_.stop()  # ensure sound has stopped at end of routine
    Training_Block1.addData('AudCorr_.started', AudCorr_.tStartRefresh)
    Training_Block1.addData('AudCorr_.stopped', AudCorr_.tStopRefresh)
    AudIncorr_.stop()  # ensure sound has stopped at end of routine
    Training_Block1.addData('AudIncorr_.started', AudIncorr_.tStartRefresh)
    Training_Block1.addData('AudIncorr_.stopped', AudIncorr_.tStopRefresh)
    Training_Block1.addData('CorrImg.started', CorrImg.tStartRefresh)
    Training_Block1.addData('CorrImg.stopped', CorrImg.tStopRefresh)
    Training_Block1.addData('IncorrImg.started', IncorrImg.tStartRefresh)
    Training_Block1.addData('IncorrImg.stopped', IncorrImg.tStopRefresh)
    # the Routine "Feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Training_Block1'


# set up handler to look after randomisation of conditions etc
Training_Block2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(training_file2),
    seed=None, name='Training_Block2')
thisExp.addLoop(Training_Block2)  # add the loop to the experiment
thisTraining_Block2 = Training_Block2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTraining_Block2.rgb)
if thisTraining_Block2 != None:
    for paramName in thisTraining_Block2:
        exec('{} = thisTraining_Block2[paramName]'.format(paramName))

for thisTraining_Block2 in Training_Block2:
    currentLoop = Training_Block2
    # abbreviate parameter names if possible (e.g. rgb = thisTraining_Block2.rgb)
    if thisTraining_Block2 != None:
        for paramName in thisTraining_Block2:
            exec('{} = thisTraining_Block2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Threat_NoThreat"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    Stim.setImage(Stimuli)
    Response.keys = []
    Response.rt = []
    _Response_allKeys = []
    # keep track of which components have finished
    Threat_NoThreatComponents = [Fixation, Stim, Response, Fixation2_2]
    for thisComponent in Threat_NoThreatComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Threat_NoThreatClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Threat_NoThreat"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Threat_NoThreatClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Threat_NoThreatClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        if Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                Fixation.setAutoDraw(False)
        
        # *Stim* updates
        if Stim.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Stim.frameNStart = frameN  # exact frame index
            Stim.tStart = t  # local t and not account for scr refresh
            Stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
            Stim.setAutoDraw(True)
        if Stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Stim.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                Stim.tStop = t  # not accounting for scr refresh
                Stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Stim, 'tStopRefresh')  # time at next scr refresh
                Stim.setAutoDraw(False)
        
        # *Response* updates
        waitOnFlip = False
        if Response.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Response.frameNStart = frameN  # exact frame index
            Response.tStart = t  # local t and not account for scr refresh
            Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response, 'tStartRefresh')  # time at next scr refresh
            Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Response.clock.reset)  # t=0 on next screen flip
        if Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                Response.tStop = t  # not accounting for scr refresh
                Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Response, 'tStopRefresh')  # time at next scr refresh
                Response.status = FINISHED
        if Response.status == STARTED and not waitOnFlip:
            theseKeys = Response.getKeys(keyList=['a', 'l'], waitRelease=False)
            _Response_allKeys.extend(theseKeys)
            if len(_Response_allKeys):
                Response.keys = _Response_allKeys[-1].name  # just the last key pressed
                Response.rt = _Response_allKeys[-1].rt
                # was this correct?
                if (Response.keys == str(CorrectAns)) or (Response.keys == CorrectAns):
                    Response.corr = 1
                else:
                    Response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *Fixation2_2* updates
        if Fixation2_2.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation2_2.frameNStart = frameN  # exact frame index
            Fixation2_2.tStart = t  # local t and not account for scr refresh
            Fixation2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation2_2, 'tStartRefresh')  # time at next scr refresh
            Fixation2_2.setAutoDraw(True)
        if Fixation2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation2_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Fixation2_2.tStop = t  # not accounting for scr refresh
                Fixation2_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation2_2, 'tStopRefresh')  # time at next scr refresh
                Fixation2_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Threat_NoThreatComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Threat_NoThreat"-------
    for thisComponent in Threat_NoThreatComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Training_Block2.addData('Fixation.started', Fixation.tStartRefresh)
    Training_Block2.addData('Fixation.stopped', Fixation.tStopRefresh)
    Training_Block2.addData('Stim.started', Stim.tStartRefresh)
    Training_Block2.addData('Stim.stopped', Stim.tStopRefresh)
    # check responses
    if Response.keys in ['', [], None]:  # No response was made
        Response.keys = None
        # was no response the correct answer?!
        if str(CorrectAns).lower() == 'none':
           Response.corr = 1;  # correct non-response
        else:
           Response.corr = 0;  # failed to respond (incorrectly)
    # store data for Training_Block2 (TrialHandler)
    Training_Block2.addData('Response.keys',Response.keys)
    Training_Block2.addData('Response.corr', Response.corr)
    if Response.keys != None:  # we had a response
        Training_Block2.addData('Response.rt', Response.rt)
    Training_Block2.addData('Response.started', Response.tStartRefresh)
    Training_Block2.addData('Response.stopped', Response.tStopRefresh)
    Training_Block2.addData('Fixation2_2.started', Fixation2_2.tStartRefresh)
    Training_Block2.addData('Fixation2_2.stopped', Fixation2_2.tStopRefresh)
    
    # ------Prepare to start Routine "Feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    Stimuli_1.setImage(Stimuli)
    #if Threat == 'Y' and Response.corr == True:
    #    AudioCorr_Threat.play()
    #elif Threat == 'Y' and Response.corr == False:
    #    AudioIncorr_Threat.play()
    #elif Threat == 'N' and Response.corr == True:
    #    AudioCorr_NoThreat.play()
    #    VisCorr_.opacity = 0.0
    #elif Threat == 'N' and Response.corr == False:
    #    AudioIncorr_NoThreat.play()
    #    VisIncorr_.opacity = 0.0
    AudCorr_.setSound(AudioCorr, secs=3, hamming=True)
    AudCorr_.setVolume(1.0, log=False)
    AudIncorr_.setSound(AudioIncorr, secs=3, hamming=True)
    AudIncorr_.setVolume(1.0, log=False)
    CorrImg.setOpacity(Opacity)
    CorrImg.setPos(Location)
    IncorrImg.setOpacity(Opacity)
    IncorrImg.setPos(Location)
    # keep track of which components have finished
    FeedbackComponents = [Stimuli_1, AudCorr_, AudIncorr_, CorrImg, IncorrImg]
    for thisComponent in FeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Feedback"-------
    while continueRoutine:
        # get current time
        t = FeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Stimuli_1* updates
        if Stimuli_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Stimuli_1.frameNStart = frameN  # exact frame index
            Stimuli_1.tStart = t  # local t and not account for scr refresh
            Stimuli_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stimuli_1, 'tStartRefresh')  # time at next scr refresh
            Stimuli_1.setAutoDraw(True)
        if Stimuli_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Stimuli_1.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                Stimuli_1.tStop = t  # not accounting for scr refresh
                Stimuli_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Stimuli_1, 'tStopRefresh')  # time at next scr refresh
                Stimuli_1.setAutoDraw(False)
        if t >= 5:
            continueRoutine = False
        # start/stop AudCorr_
        if AudCorr_.status == NOT_STARTED and Response.corr == True:
            # keep track of start time/frame for later
            AudCorr_.frameNStart = frameN  # exact frame index
            AudCorr_.tStart = t  # local t and not account for scr refresh
            AudCorr_.tStartRefresh = tThisFlipGlobal  # on global time
            AudCorr_.play(when=win)  # sync with win flip
        if AudCorr_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > AudCorr_.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                AudCorr_.tStop = t  # not accounting for scr refresh
                AudCorr_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(AudCorr_, 'tStopRefresh')  # time at next scr refresh
                AudCorr_.stop()
        # start/stop AudIncorr_
        if AudIncorr_.status == NOT_STARTED and Response.corr == False:
            # keep track of start time/frame for later
            AudIncorr_.frameNStart = frameN  # exact frame index
            AudIncorr_.tStart = t  # local t and not account for scr refresh
            AudIncorr_.tStartRefresh = tThisFlipGlobal  # on global time
            AudIncorr_.play(when=win)  # sync with win flip
        if AudIncorr_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > AudIncorr_.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                AudIncorr_.tStop = t  # not accounting for scr refresh
                AudIncorr_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(AudIncorr_, 'tStopRefresh')  # time at next scr refresh
                AudIncorr_.stop()
        
        # *CorrImg* updates
        if CorrImg.status == NOT_STARTED and Response.corr == True:
            # keep track of start time/frame for later
            CorrImg.frameNStart = frameN  # exact frame index
            CorrImg.tStart = t  # local t and not account for scr refresh
            CorrImg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CorrImg, 'tStartRefresh')  # time at next scr refresh
            CorrImg.setAutoDraw(True)
        if CorrImg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CorrImg.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                CorrImg.tStop = t  # not accounting for scr refresh
                CorrImg.frameNStop = frameN  # exact frame index
                win.timeOnFlip(CorrImg, 'tStopRefresh')  # time at next scr refresh
                CorrImg.setAutoDraw(False)
        
        # *IncorrImg* updates
        if IncorrImg.status == NOT_STARTED and Response.corr == False:
            # keep track of start time/frame for later
            IncorrImg.frameNStart = frameN  # exact frame index
            IncorrImg.tStart = t  # local t and not account for scr refresh
            IncorrImg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IncorrImg, 'tStartRefresh')  # time at next scr refresh
            IncorrImg.setAutoDraw(True)
        if IncorrImg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > IncorrImg.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                IncorrImg.tStop = t  # not accounting for scr refresh
                IncorrImg.frameNStop = frameN  # exact frame index
                win.timeOnFlip(IncorrImg, 'tStopRefresh')  # time at next scr refresh
                IncorrImg.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Training_Block2.addData('Stimuli_1.started', Stimuli_1.tStartRefresh)
    Training_Block2.addData('Stimuli_1.stopped', Stimuli_1.tStopRefresh)
    AudCorr_.stop()  # ensure sound has stopped at end of routine
    Training_Block2.addData('AudCorr_.started', AudCorr_.tStartRefresh)
    Training_Block2.addData('AudCorr_.stopped', AudCorr_.tStopRefresh)
    AudIncorr_.stop()  # ensure sound has stopped at end of routine
    Training_Block2.addData('AudIncorr_.started', AudIncorr_.tStartRefresh)
    Training_Block2.addData('AudIncorr_.stopped', AudIncorr_.tStopRefresh)
    Training_Block2.addData('CorrImg.started', CorrImg.tStartRefresh)
    Training_Block2.addData('CorrImg.stopped', CorrImg.tStopRefresh)
    Training_Block2.addData('IncorrImg.started', IncorrImg.tStartRefresh)
    Training_Block2.addData('IncorrImg.stopped', IncorrImg.tStopRefresh)
    # the Routine "Feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Training_Block2'


# set up handler to look after randomisation of conditions etc
Training_Block3 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(training_file3),
    seed=None, name='Training_Block3')
thisExp.addLoop(Training_Block3)  # add the loop to the experiment
thisTraining_Block3 = Training_Block3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTraining_Block3.rgb)
if thisTraining_Block3 != None:
    for paramName in thisTraining_Block3:
        exec('{} = thisTraining_Block3[paramName]'.format(paramName))

for thisTraining_Block3 in Training_Block3:
    currentLoop = Training_Block3
    # abbreviate parameter names if possible (e.g. rgb = thisTraining_Block3.rgb)
    if thisTraining_Block3 != None:
        for paramName in thisTraining_Block3:
            exec('{} = thisTraining_Block3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Threat_NoThreat"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    Stim.setImage(Stimuli)
    Response.keys = []
    Response.rt = []
    _Response_allKeys = []
    # keep track of which components have finished
    Threat_NoThreatComponents = [Fixation, Stim, Response, Fixation2_2]
    for thisComponent in Threat_NoThreatComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Threat_NoThreatClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Threat_NoThreat"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Threat_NoThreatClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Threat_NoThreatClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        if Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                Fixation.setAutoDraw(False)
        
        # *Stim* updates
        if Stim.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Stim.frameNStart = frameN  # exact frame index
            Stim.tStart = t  # local t and not account for scr refresh
            Stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
            Stim.setAutoDraw(True)
        if Stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Stim.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                Stim.tStop = t  # not accounting for scr refresh
                Stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Stim, 'tStopRefresh')  # time at next scr refresh
                Stim.setAutoDraw(False)
        
        # *Response* updates
        waitOnFlip = False
        if Response.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Response.frameNStart = frameN  # exact frame index
            Response.tStart = t  # local t and not account for scr refresh
            Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response, 'tStartRefresh')  # time at next scr refresh
            Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Response.clock.reset)  # t=0 on next screen flip
        if Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                Response.tStop = t  # not accounting for scr refresh
                Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Response, 'tStopRefresh')  # time at next scr refresh
                Response.status = FINISHED
        if Response.status == STARTED and not waitOnFlip:
            theseKeys = Response.getKeys(keyList=['a', 'l'], waitRelease=False)
            _Response_allKeys.extend(theseKeys)
            if len(_Response_allKeys):
                Response.keys = _Response_allKeys[-1].name  # just the last key pressed
                Response.rt = _Response_allKeys[-1].rt
                # was this correct?
                if (Response.keys == str(CorrectAns)) or (Response.keys == CorrectAns):
                    Response.corr = 1
                else:
                    Response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *Fixation2_2* updates
        if Fixation2_2.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation2_2.frameNStart = frameN  # exact frame index
            Fixation2_2.tStart = t  # local t and not account for scr refresh
            Fixation2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation2_2, 'tStartRefresh')  # time at next scr refresh
            Fixation2_2.setAutoDraw(True)
        if Fixation2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation2_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Fixation2_2.tStop = t  # not accounting for scr refresh
                Fixation2_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation2_2, 'tStopRefresh')  # time at next scr refresh
                Fixation2_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Threat_NoThreatComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Threat_NoThreat"-------
    for thisComponent in Threat_NoThreatComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Training_Block3.addData('Fixation.started', Fixation.tStartRefresh)
    Training_Block3.addData('Fixation.stopped', Fixation.tStopRefresh)
    Training_Block3.addData('Stim.started', Stim.tStartRefresh)
    Training_Block3.addData('Stim.stopped', Stim.tStopRefresh)
    # check responses
    if Response.keys in ['', [], None]:  # No response was made
        Response.keys = None
        # was no response the correct answer?!
        if str(CorrectAns).lower() == 'none':
           Response.corr = 1;  # correct non-response
        else:
           Response.corr = 0;  # failed to respond (incorrectly)
    # store data for Training_Block3 (TrialHandler)
    Training_Block3.addData('Response.keys',Response.keys)
    Training_Block3.addData('Response.corr', Response.corr)
    if Response.keys != None:  # we had a response
        Training_Block3.addData('Response.rt', Response.rt)
    Training_Block3.addData('Response.started', Response.tStartRefresh)
    Training_Block3.addData('Response.stopped', Response.tStopRefresh)
    Training_Block3.addData('Fixation2_2.started', Fixation2_2.tStartRefresh)
    Training_Block3.addData('Fixation2_2.stopped', Fixation2_2.tStopRefresh)
    
    # ------Prepare to start Routine "Feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    Stimuli_1.setImage(Stimuli)
    #if Threat == 'Y' and Response.corr == True:
    #    AudioCorr_Threat.play()
    #elif Threat == 'Y' and Response.corr == False:
    #    AudioIncorr_Threat.play()
    #elif Threat == 'N' and Response.corr == True:
    #    AudioCorr_NoThreat.play()
    #    VisCorr_.opacity = 0.0
    #elif Threat == 'N' and Response.corr == False:
    #    AudioIncorr_NoThreat.play()
    #    VisIncorr_.opacity = 0.0
    AudCorr_.setSound(AudioCorr, secs=3, hamming=True)
    AudCorr_.setVolume(1.0, log=False)
    AudIncorr_.setSound(AudioIncorr, secs=3, hamming=True)
    AudIncorr_.setVolume(1.0, log=False)
    CorrImg.setOpacity(Opacity)
    CorrImg.setPos(Location)
    IncorrImg.setOpacity(Opacity)
    IncorrImg.setPos(Location)
    # keep track of which components have finished
    FeedbackComponents = [Stimuli_1, AudCorr_, AudIncorr_, CorrImg, IncorrImg]
    for thisComponent in FeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Feedback"-------
    while continueRoutine:
        # get current time
        t = FeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Stimuli_1* updates
        if Stimuli_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Stimuli_1.frameNStart = frameN  # exact frame index
            Stimuli_1.tStart = t  # local t and not account for scr refresh
            Stimuli_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stimuli_1, 'tStartRefresh')  # time at next scr refresh
            Stimuli_1.setAutoDraw(True)
        if Stimuli_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Stimuli_1.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                Stimuli_1.tStop = t  # not accounting for scr refresh
                Stimuli_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Stimuli_1, 'tStopRefresh')  # time at next scr refresh
                Stimuli_1.setAutoDraw(False)
        if t >= 5:
            continueRoutine = False
        # start/stop AudCorr_
        if AudCorr_.status == NOT_STARTED and Response.corr == True:
            # keep track of start time/frame for later
            AudCorr_.frameNStart = frameN  # exact frame index
            AudCorr_.tStart = t  # local t and not account for scr refresh
            AudCorr_.tStartRefresh = tThisFlipGlobal  # on global time
            AudCorr_.play(when=win)  # sync with win flip
        if AudCorr_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > AudCorr_.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                AudCorr_.tStop = t  # not accounting for scr refresh
                AudCorr_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(AudCorr_, 'tStopRefresh')  # time at next scr refresh
                AudCorr_.stop()
        # start/stop AudIncorr_
        if AudIncorr_.status == NOT_STARTED and Response.corr == False:
            # keep track of start time/frame for later
            AudIncorr_.frameNStart = frameN  # exact frame index
            AudIncorr_.tStart = t  # local t and not account for scr refresh
            AudIncorr_.tStartRefresh = tThisFlipGlobal  # on global time
            AudIncorr_.play(when=win)  # sync with win flip
        if AudIncorr_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > AudIncorr_.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                AudIncorr_.tStop = t  # not accounting for scr refresh
                AudIncorr_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(AudIncorr_, 'tStopRefresh')  # time at next scr refresh
                AudIncorr_.stop()
        
        # *CorrImg* updates
        if CorrImg.status == NOT_STARTED and Response.corr == True:
            # keep track of start time/frame for later
            CorrImg.frameNStart = frameN  # exact frame index
            CorrImg.tStart = t  # local t and not account for scr refresh
            CorrImg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CorrImg, 'tStartRefresh')  # time at next scr refresh
            CorrImg.setAutoDraw(True)
        if CorrImg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CorrImg.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                CorrImg.tStop = t  # not accounting for scr refresh
                CorrImg.frameNStop = frameN  # exact frame index
                win.timeOnFlip(CorrImg, 'tStopRefresh')  # time at next scr refresh
                CorrImg.setAutoDraw(False)
        
        # *IncorrImg* updates
        if IncorrImg.status == NOT_STARTED and Response.corr == False:
            # keep track of start time/frame for later
            IncorrImg.frameNStart = frameN  # exact frame index
            IncorrImg.tStart = t  # local t and not account for scr refresh
            IncorrImg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IncorrImg, 'tStartRefresh')  # time at next scr refresh
            IncorrImg.setAutoDraw(True)
        if IncorrImg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > IncorrImg.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                IncorrImg.tStop = t  # not accounting for scr refresh
                IncorrImg.frameNStop = frameN  # exact frame index
                win.timeOnFlip(IncorrImg, 'tStopRefresh')  # time at next scr refresh
                IncorrImg.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Training_Block3.addData('Stimuli_1.started', Stimuli_1.tStartRefresh)
    Training_Block3.addData('Stimuli_1.stopped', Stimuli_1.tStopRefresh)
    AudCorr_.stop()  # ensure sound has stopped at end of routine
    Training_Block3.addData('AudCorr_.started', AudCorr_.tStartRefresh)
    Training_Block3.addData('AudCorr_.stopped', AudCorr_.tStopRefresh)
    AudIncorr_.stop()  # ensure sound has stopped at end of routine
    Training_Block3.addData('AudIncorr_.started', AudIncorr_.tStartRefresh)
    Training_Block3.addData('AudIncorr_.stopped', AudIncorr_.tStopRefresh)
    Training_Block3.addData('CorrImg.started', CorrImg.tStartRefresh)
    Training_Block3.addData('CorrImg.stopped', CorrImg.tStopRefresh)
    Training_Block3.addData('IncorrImg.started', IncorrImg.tStartRefresh)
    Training_Block3.addData('IncorrImg.stopped', IncorrImg.tStopRefresh)
    # the Routine "Feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Training_Block3'


# set up handler to look after randomisation of conditions etc
Training_Block4 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(training_file4),
    seed=None, name='Training_Block4')
thisExp.addLoop(Training_Block4)  # add the loop to the experiment
thisTraining_Block4 = Training_Block4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTraining_Block4.rgb)
if thisTraining_Block4 != None:
    for paramName in thisTraining_Block4:
        exec('{} = thisTraining_Block4[paramName]'.format(paramName))

for thisTraining_Block4 in Training_Block4:
    currentLoop = Training_Block4
    # abbreviate parameter names if possible (e.g. rgb = thisTraining_Block4.rgb)
    if thisTraining_Block4 != None:
        for paramName in thisTraining_Block4:
            exec('{} = thisTraining_Block4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Threat_NoThreat"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    Stim.setImage(Stimuli)
    Response.keys = []
    Response.rt = []
    _Response_allKeys = []
    # keep track of which components have finished
    Threat_NoThreatComponents = [Fixation, Stim, Response, Fixation2_2]
    for thisComponent in Threat_NoThreatComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Threat_NoThreatClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Threat_NoThreat"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Threat_NoThreatClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Threat_NoThreatClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        if Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                Fixation.setAutoDraw(False)
        
        # *Stim* updates
        if Stim.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Stim.frameNStart = frameN  # exact frame index
            Stim.tStart = t  # local t and not account for scr refresh
            Stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
            Stim.setAutoDraw(True)
        if Stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Stim.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                Stim.tStop = t  # not accounting for scr refresh
                Stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Stim, 'tStopRefresh')  # time at next scr refresh
                Stim.setAutoDraw(False)
        
        # *Response* updates
        waitOnFlip = False
        if Response.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Response.frameNStart = frameN  # exact frame index
            Response.tStart = t  # local t and not account for scr refresh
            Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response, 'tStartRefresh')  # time at next scr refresh
            Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Response.clock.reset)  # t=0 on next screen flip
        if Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                Response.tStop = t  # not accounting for scr refresh
                Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Response, 'tStopRefresh')  # time at next scr refresh
                Response.status = FINISHED
        if Response.status == STARTED and not waitOnFlip:
            theseKeys = Response.getKeys(keyList=['a', 'l'], waitRelease=False)
            _Response_allKeys.extend(theseKeys)
            if len(_Response_allKeys):
                Response.keys = _Response_allKeys[-1].name  # just the last key pressed
                Response.rt = _Response_allKeys[-1].rt
                # was this correct?
                if (Response.keys == str(CorrectAns)) or (Response.keys == CorrectAns):
                    Response.corr = 1
                else:
                    Response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *Fixation2_2* updates
        if Fixation2_2.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation2_2.frameNStart = frameN  # exact frame index
            Fixation2_2.tStart = t  # local t and not account for scr refresh
            Fixation2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation2_2, 'tStartRefresh')  # time at next scr refresh
            Fixation2_2.setAutoDraw(True)
        if Fixation2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation2_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Fixation2_2.tStop = t  # not accounting for scr refresh
                Fixation2_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation2_2, 'tStopRefresh')  # time at next scr refresh
                Fixation2_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Threat_NoThreatComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Threat_NoThreat"-------
    for thisComponent in Threat_NoThreatComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Training_Block4.addData('Fixation.started', Fixation.tStartRefresh)
    Training_Block4.addData('Fixation.stopped', Fixation.tStopRefresh)
    Training_Block4.addData('Stim.started', Stim.tStartRefresh)
    Training_Block4.addData('Stim.stopped', Stim.tStopRefresh)
    # check responses
    if Response.keys in ['', [], None]:  # No response was made
        Response.keys = None
        # was no response the correct answer?!
        if str(CorrectAns).lower() == 'none':
           Response.corr = 1;  # correct non-response
        else:
           Response.corr = 0;  # failed to respond (incorrectly)
    # store data for Training_Block4 (TrialHandler)
    Training_Block4.addData('Response.keys',Response.keys)
    Training_Block4.addData('Response.corr', Response.corr)
    if Response.keys != None:  # we had a response
        Training_Block4.addData('Response.rt', Response.rt)
    Training_Block4.addData('Response.started', Response.tStartRefresh)
    Training_Block4.addData('Response.stopped', Response.tStopRefresh)
    Training_Block4.addData('Fixation2_2.started', Fixation2_2.tStartRefresh)
    Training_Block4.addData('Fixation2_2.stopped', Fixation2_2.tStopRefresh)
    
    # ------Prepare to start Routine "Feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    Stimuli_1.setImage(Stimuli)
    #if Threat == 'Y' and Response.corr == True:
    #    AudioCorr_Threat.play()
    #elif Threat == 'Y' and Response.corr == False:
    #    AudioIncorr_Threat.play()
    #elif Threat == 'N' and Response.corr == True:
    #    AudioCorr_NoThreat.play()
    #    VisCorr_.opacity = 0.0
    #elif Threat == 'N' and Response.corr == False:
    #    AudioIncorr_NoThreat.play()
    #    VisIncorr_.opacity = 0.0
    AudCorr_.setSound(AudioCorr, secs=3, hamming=True)
    AudCorr_.setVolume(1.0, log=False)
    AudIncorr_.setSound(AudioIncorr, secs=3, hamming=True)
    AudIncorr_.setVolume(1.0, log=False)
    CorrImg.setOpacity(Opacity)
    CorrImg.setPos(Location)
    IncorrImg.setOpacity(Opacity)
    IncorrImg.setPos(Location)
    # keep track of which components have finished
    FeedbackComponents = [Stimuli_1, AudCorr_, AudIncorr_, CorrImg, IncorrImg]
    for thisComponent in FeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Feedback"-------
    while continueRoutine:
        # get current time
        t = FeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Stimuli_1* updates
        if Stimuli_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Stimuli_1.frameNStart = frameN  # exact frame index
            Stimuli_1.tStart = t  # local t and not account for scr refresh
            Stimuli_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stimuli_1, 'tStartRefresh')  # time at next scr refresh
            Stimuli_1.setAutoDraw(True)
        if Stimuli_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Stimuli_1.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                Stimuli_1.tStop = t  # not accounting for scr refresh
                Stimuli_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Stimuli_1, 'tStopRefresh')  # time at next scr refresh
                Stimuli_1.setAutoDraw(False)
        if t >= 5:
            continueRoutine = False
        # start/stop AudCorr_
        if AudCorr_.status == NOT_STARTED and Response.corr == True:
            # keep track of start time/frame for later
            AudCorr_.frameNStart = frameN  # exact frame index
            AudCorr_.tStart = t  # local t and not account for scr refresh
            AudCorr_.tStartRefresh = tThisFlipGlobal  # on global time
            AudCorr_.play(when=win)  # sync with win flip
        if AudCorr_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > AudCorr_.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                AudCorr_.tStop = t  # not accounting for scr refresh
                AudCorr_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(AudCorr_, 'tStopRefresh')  # time at next scr refresh
                AudCorr_.stop()
        # start/stop AudIncorr_
        if AudIncorr_.status == NOT_STARTED and Response.corr == False:
            # keep track of start time/frame for later
            AudIncorr_.frameNStart = frameN  # exact frame index
            AudIncorr_.tStart = t  # local t and not account for scr refresh
            AudIncorr_.tStartRefresh = tThisFlipGlobal  # on global time
            AudIncorr_.play(when=win)  # sync with win flip
        if AudIncorr_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > AudIncorr_.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                AudIncorr_.tStop = t  # not accounting for scr refresh
                AudIncorr_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(AudIncorr_, 'tStopRefresh')  # time at next scr refresh
                AudIncorr_.stop()
        
        # *CorrImg* updates
        if CorrImg.status == NOT_STARTED and Response.corr == True:
            # keep track of start time/frame for later
            CorrImg.frameNStart = frameN  # exact frame index
            CorrImg.tStart = t  # local t and not account for scr refresh
            CorrImg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CorrImg, 'tStartRefresh')  # time at next scr refresh
            CorrImg.setAutoDraw(True)
        if CorrImg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CorrImg.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                CorrImg.tStop = t  # not accounting for scr refresh
                CorrImg.frameNStop = frameN  # exact frame index
                win.timeOnFlip(CorrImg, 'tStopRefresh')  # time at next scr refresh
                CorrImg.setAutoDraw(False)
        
        # *IncorrImg* updates
        if IncorrImg.status == NOT_STARTED and Response.corr == False:
            # keep track of start time/frame for later
            IncorrImg.frameNStart = frameN  # exact frame index
            IncorrImg.tStart = t  # local t and not account for scr refresh
            IncorrImg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IncorrImg, 'tStartRefresh')  # time at next scr refresh
            IncorrImg.setAutoDraw(True)
        if IncorrImg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > IncorrImg.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                IncorrImg.tStop = t  # not accounting for scr refresh
                IncorrImg.frameNStop = frameN  # exact frame index
                win.timeOnFlip(IncorrImg, 'tStopRefresh')  # time at next scr refresh
                IncorrImg.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Training_Block4.addData('Stimuli_1.started', Stimuli_1.tStartRefresh)
    Training_Block4.addData('Stimuli_1.stopped', Stimuli_1.tStopRefresh)
    AudCorr_.stop()  # ensure sound has stopped at end of routine
    Training_Block4.addData('AudCorr_.started', AudCorr_.tStartRefresh)
    Training_Block4.addData('AudCorr_.stopped', AudCorr_.tStopRefresh)
    AudIncorr_.stop()  # ensure sound has stopped at end of routine
    Training_Block4.addData('AudIncorr_.started', AudIncorr_.tStartRefresh)
    Training_Block4.addData('AudIncorr_.stopped', AudIncorr_.tStopRefresh)
    Training_Block4.addData('CorrImg.started', CorrImg.tStartRefresh)
    Training_Block4.addData('CorrImg.stopped', CorrImg.tStopRefresh)
    Training_Block4.addData('IncorrImg.started', IncorrImg.tStartRefresh)
    Training_Block4.addData('IncorrImg.stopped', IncorrImg.tStopRefresh)
    # the Routine "Feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Training_Block4'


# set up handler to look after randomisation of conditions etc
Test1 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(Test_file1),
    seed=None, name='Test1')
thisExp.addLoop(Test1)  # add the loop to the experiment
thisTest1 = Test1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest1.rgb)
if thisTest1 != None:
    for paramName in thisTest1:
        exec('{} = thisTest1[paramName]'.format(paramName))

for thisTest1 in Test1:
    currentLoop = Test1
    # abbreviate parameter names if possible (e.g. rgb = thisTest1.rgb)
    if thisTest1 != None:
        for paramName in thisTest1:
            exec('{} = thisTest1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Threat_NoThreat"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    Stim.setImage(Stimuli)
    Response.keys = []
    Response.rt = []
    _Response_allKeys = []
    # keep track of which components have finished
    Threat_NoThreatComponents = [Fixation, Stim, Response, Fixation2_2]
    for thisComponent in Threat_NoThreatComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Threat_NoThreatClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Threat_NoThreat"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Threat_NoThreatClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Threat_NoThreatClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        if Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                Fixation.setAutoDraw(False)
        
        # *Stim* updates
        if Stim.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Stim.frameNStart = frameN  # exact frame index
            Stim.tStart = t  # local t and not account for scr refresh
            Stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
            Stim.setAutoDraw(True)
        if Stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Stim.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                Stim.tStop = t  # not accounting for scr refresh
                Stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Stim, 'tStopRefresh')  # time at next scr refresh
                Stim.setAutoDraw(False)
        
        # *Response* updates
        waitOnFlip = False
        if Response.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Response.frameNStart = frameN  # exact frame index
            Response.tStart = t  # local t and not account for scr refresh
            Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response, 'tStartRefresh')  # time at next scr refresh
            Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Response.clock.reset)  # t=0 on next screen flip
        if Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                Response.tStop = t  # not accounting for scr refresh
                Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Response, 'tStopRefresh')  # time at next scr refresh
                Response.status = FINISHED
        if Response.status == STARTED and not waitOnFlip:
            theseKeys = Response.getKeys(keyList=['a', 'l'], waitRelease=False)
            _Response_allKeys.extend(theseKeys)
            if len(_Response_allKeys):
                Response.keys = _Response_allKeys[-1].name  # just the last key pressed
                Response.rt = _Response_allKeys[-1].rt
                # was this correct?
                if (Response.keys == str(CorrectAns)) or (Response.keys == CorrectAns):
                    Response.corr = 1
                else:
                    Response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *Fixation2_2* updates
        if Fixation2_2.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation2_2.frameNStart = frameN  # exact frame index
            Fixation2_2.tStart = t  # local t and not account for scr refresh
            Fixation2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation2_2, 'tStartRefresh')  # time at next scr refresh
            Fixation2_2.setAutoDraw(True)
        if Fixation2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation2_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Fixation2_2.tStop = t  # not accounting for scr refresh
                Fixation2_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation2_2, 'tStopRefresh')  # time at next scr refresh
                Fixation2_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Threat_NoThreatComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Threat_NoThreat"-------
    for thisComponent in Threat_NoThreatComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Test1.addData('Fixation.started', Fixation.tStartRefresh)
    Test1.addData('Fixation.stopped', Fixation.tStopRefresh)
    Test1.addData('Stim.started', Stim.tStartRefresh)
    Test1.addData('Stim.stopped', Stim.tStopRefresh)
    # check responses
    if Response.keys in ['', [], None]:  # No response was made
        Response.keys = None
        # was no response the correct answer?!
        if str(CorrectAns).lower() == 'none':
           Response.corr = 1;  # correct non-response
        else:
           Response.corr = 0;  # failed to respond (incorrectly)
    # store data for Test1 (TrialHandler)
    Test1.addData('Response.keys',Response.keys)
    Test1.addData('Response.corr', Response.corr)
    if Response.keys != None:  # we had a response
        Test1.addData('Response.rt', Response.rt)
    Test1.addData('Response.started', Response.tStartRefresh)
    Test1.addData('Response.stopped', Response.tStopRefresh)
    Test1.addData('Fixation2_2.started', Fixation2_2.tStartRefresh)
    Test1.addData('Fixation2_2.stopped', Fixation2_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Test1'


# set up handler to look after randomisation of conditions etc
Test2 = data.TrialHandler(nReps=None, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(Test_file2),
    seed=None, name='Test2')
thisExp.addLoop(Test2)  # add the loop to the experiment
thisTest2 = Test2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest2.rgb)
if thisTest2 != None:
    for paramName in thisTest2:
        exec('{} = thisTest2[paramName]'.format(paramName))

for thisTest2 in Test2:
    currentLoop = Test2
    # abbreviate parameter names if possible (e.g. rgb = thisTest2.rgb)
    if thisTest2 != None:
        for paramName in thisTest2:
            exec('{} = thisTest2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Threat_NoThreat"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    Stim.setImage(Stimuli)
    Response.keys = []
    Response.rt = []
    _Response_allKeys = []
    # keep track of which components have finished
    Threat_NoThreatComponents = [Fixation, Stim, Response, Fixation2_2]
    for thisComponent in Threat_NoThreatComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Threat_NoThreatClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Threat_NoThreat"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Threat_NoThreatClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Threat_NoThreatClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        if Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                Fixation.setAutoDraw(False)
        
        # *Stim* updates
        if Stim.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Stim.frameNStart = frameN  # exact frame index
            Stim.tStart = t  # local t and not account for scr refresh
            Stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
            Stim.setAutoDraw(True)
        if Stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Stim.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                Stim.tStop = t  # not accounting for scr refresh
                Stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Stim, 'tStopRefresh')  # time at next scr refresh
                Stim.setAutoDraw(False)
        
        # *Response* updates
        waitOnFlip = False
        if Response.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Response.frameNStart = frameN  # exact frame index
            Response.tStart = t  # local t and not account for scr refresh
            Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response, 'tStartRefresh')  # time at next scr refresh
            Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Response.clock.reset)  # t=0 on next screen flip
        if Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                Response.tStop = t  # not accounting for scr refresh
                Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Response, 'tStopRefresh')  # time at next scr refresh
                Response.status = FINISHED
        if Response.status == STARTED and not waitOnFlip:
            theseKeys = Response.getKeys(keyList=['a', 'l'], waitRelease=False)
            _Response_allKeys.extend(theseKeys)
            if len(_Response_allKeys):
                Response.keys = _Response_allKeys[-1].name  # just the last key pressed
                Response.rt = _Response_allKeys[-1].rt
                # was this correct?
                if (Response.keys == str(CorrectAns)) or (Response.keys == CorrectAns):
                    Response.corr = 1
                else:
                    Response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *Fixation2_2* updates
        if Fixation2_2.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation2_2.frameNStart = frameN  # exact frame index
            Fixation2_2.tStart = t  # local t and not account for scr refresh
            Fixation2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation2_2, 'tStartRefresh')  # time at next scr refresh
            Fixation2_2.setAutoDraw(True)
        if Fixation2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation2_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Fixation2_2.tStop = t  # not accounting for scr refresh
                Fixation2_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation2_2, 'tStopRefresh')  # time at next scr refresh
                Fixation2_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Threat_NoThreatComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Threat_NoThreat"-------
    for thisComponent in Threat_NoThreatComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Test2.addData('Fixation.started', Fixation.tStartRefresh)
    Test2.addData('Fixation.stopped', Fixation.tStopRefresh)
    Test2.addData('Stim.started', Stim.tStartRefresh)
    Test2.addData('Stim.stopped', Stim.tStopRefresh)
    # check responses
    if Response.keys in ['', [], None]:  # No response was made
        Response.keys = None
        # was no response the correct answer?!
        if str(CorrectAns).lower() == 'none':
           Response.corr = 1;  # correct non-response
        else:
           Response.corr = 0;  # failed to respond (incorrectly)
    # store data for Test2 (TrialHandler)
    Test2.addData('Response.keys',Response.keys)
    Test2.addData('Response.corr', Response.corr)
    if Response.keys != None:  # we had a response
        Test2.addData('Response.rt', Response.rt)
    Test2.addData('Response.started', Response.tStartRefresh)
    Test2.addData('Response.stopped', Response.tStopRefresh)
    Test2.addData('Fixation2_2.started', Fixation2_2.tStartRefresh)
    Test2.addData('Fixation2_2.stopped', Fixation2_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed None repeats of 'Test2'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
