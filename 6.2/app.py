from app_modules import train_faces, recognize_faces
from app_graphics import menu_graphic, training_graphic, person_recognize_graphic, help_graphic


def main():
    menu_graphic()
    choice_menu = int(input())
    
    while choice_menu != 4:
        if choice_menu == 1:
            train_faces()
            training_graphic()
            input()
        elif choice_menu == 2:
            person_recognize_graphic()
            choice_person_recognize_graphic = int(input())
            if choice_person_recognize_graphic == 1:
                recognize_faces(r'C:\Users\zan1gi\Programmering\Images for lab 6.2 script\img\validation\Joe Biden\P20210303AS-1901-cropped.jpg')
            elif choice_person_recognize_graphic == 2:
                recognize_faces(r'C:\Users\zangi\Programmering\Images for lab 6.2 script\img\validation\Vladimir Putin\d96e21eb-a22e-4b8e-b4f5-65eaf7e82cc1.jpg')
            elif choice_person_recognize_graphic == 3:
                recognize_faces(r'C:\Users\zangi\Programmering\Images for lab 6.2 script\img\validation\Donald trump\Donald_Trump_official_portrait_cropped.jpg')
            elif choice_person_recognize_graphic == 4:
                recognize_faces(r'C:\Users\zangi\Programmering\Images for lab 6.2 script\img\validation\Mixed Joe Donald\1633358082.jpg')
            elif choice_person_recognize_graphic == 5:
                recognize_faces(r'C:\Users\zangi\Programmering\Images for lab 6.2 script\img\validation\Mixed Joe Vladimir\skynews-joe-biden-vladimir-putin_5394911.jpg') 
            elif choice_person_recognize_graphic == 6:
                recognize_faces(r'C:\Users\zangi\Programmering\Images for lab 6.2 script\img\validation\Mixed Donald Vladimir\f2384598-5df8-11ea-be3e-43af5536d789_image_hires_040926.jpg')     
        elif choice_menu == 3:
            help_graphic()
            input()
        else:
            print()
            print('Please select a valid choice in the menu. (1-4)')
        print()
        menu_graphic()
        choice_menu = int(input())


if __name__=='__main__':          
    main()