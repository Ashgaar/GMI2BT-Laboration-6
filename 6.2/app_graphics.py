def menu_graphic():
    print('')
    print('------------------------------------------')
    print('Facial recognition and training program')
    print('------------------------------------------')
    print()
    print('Select an OpenCV operation')
    print('[1] Face training')
    print('[2] Face recognition')
    print('[3] Help')
    print('[4] Quit')
    
def help_graphic():
    print()
    print('------------------------------------------')
    print('Help menu')
    print('------------------------------------------')
    print('Option 1 Trains faces that are currently in the program and saves the data to files (facetrained.yml, features.npy, labels.npy)')
    print('Option 2 After training this option will match the data to the faces and see if they find a match.')
    print('Hit enter to exit help')
    
def training_graphic():
    print()
    print('Traning finished and files saved')
    print('Hit enter to exit training')
    
def person_recognize_graphic():
    print()
    print('Choose one person that the program should recognize to validate the training.')
    print()
    print('[1] Joe Biden')
    print('[2] Vladimir Putin')
    print('[3] Donald Trump')
    print('[4] Mixed Joe Donald')
    print('[5] Mixed Joe Vladimir')
    print('[6] Mixed Donald Vladimir')