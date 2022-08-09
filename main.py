from kivymd.app import MDApp

from kivymd.uix.button import MDFlatButton,MDRoundFlatButton,MDIconButton

from kivy.lang.builder import Builder

from kivymd.uix.dialog import MDDialog

from kivy.uix.screenmanager import ScreenManager,Screen

screen_helper="""

ScreenManager:

    MainScreen:

        name:'Main'

    FtScreen:

        name:'Feet'

    CmScreen:

        name:'Cm'

    MScreen:

        name:'M'

    Output1Screen:

        name:'Out1'

    Output2Screen:

        name:'Out2'

    Output3Screen:

        name:'Out3'


<MainScreen>:

    

    name:'Main'

    MDLabel:

        text:"BMI CALCULATOR"

        font_size:'60sp'

        font_style:"H3"

        theme_text_color:'Error'

        pos_hint:{'center_x':0.5,'center_y':0.9}

        halign:'center'

    MDTextField:

        id:input_1

        hint_text: "Enter weight in kg"

        helper_text: "in kilograms only"

        helper_text_mode: "on_focus"

        pos_hint: {'center_x':0.5,'center_y':0.7}

        size_hint_x: None

        width: 200

    MDLabel:

        text:"Choose unit of height"

        font_size:'60sp'

        font_style:"H5"

        theme_text_color:'Error'

        pos_hint:{'center_x':0.5,'center_y':0.6}

        halign:'center'
        

    MDRoundFlatButton:

        text:"Feet Inches"

        id:button_1

        pos_hint:{'center_x':0.5,'center_y':0.5}

        on_press:root.manager.current='Feet'
        

    MDRoundFlatButton:

        text:"Centimetres"

        id:button_2

        pos_hint:{'center_x':0.5,'center_y':0.4}

        on_press:root.manager.current='Cm'
        

    MDRoundFlatButton:

        text:"Metres"

        id:button_3

        pos_hint:{'center_x':0.5,'center_y':0.3}

        on_press:root.manager.current='M'


<FtScreen>:
    

    name:'Feet'

    MDTextField:

        id:input_2

        hint_text: "Enter foot part of height"

        helper_text: ""

        helper_text_mode: "on_focus"

        pos_hint: {'center_x':0.5,'center_y':0.7}

        size_hint_x: None

        width: 200


    MDTextField:

        id:input_3

        hint_text: "Enter inches part of height"

        helper_text: "Put 0 if there is no inch part"

        helper_text_mode: "on_focus"

        pos_hint: {'center_x':0.5,'center_y':0.6}

        size_hint_x: None

        width: 200

    MDIconButton:

        icon:"chevron-triple-left"

        id:button_4

        pos_hint:{'center_x':0.1,'center_y':0.9}

        on_press:root.manager.current='Main'
        

    MDRoundFlatButton:

        text:"SUBMIT"

        id:button_7

        pos_hint:{'center_x':0.5,'center_y':0.1}

        on_press:app.submit1()
        on_press:root.manager.current='Out1'


<CmScreen>:
    

    name:'Cm'

    MDTextField:

        id:input_4

        hint_text: "Enter height in cm"

        helper_text: ""

        helper_text_mode: "on_focus"

        pos_hint: {'center_x':0.5,'center_y':0.7}

        size_hint_x: None

        width: 200

    MDIconButton:

        icon:"chevron-triple-left"

        id:button_5

        pos_hint:{'center_x':0.1,'center_y':0.9}

        on_press:root.manager.current='Main'

    MDRoundFlatButton:

        text:"SUBMIT"

        id:button_8

        pos_hint:{'center_x':0.5,'center_y':0.1}

        on_press:app.submit2()
        on_press:root.manager.current='Out2'


<MScreen>:
    

    name:'M'

    MDTextField:

        id:input_5

        hint_text: "Enter height in metres"

        helper_text: ""

        helper_text_mode: "on_focus"

        pos_hint: {'center_x':0.5,'center_y':0.7}

        size_hint_x: None

        width: 200

    MDIconButton:

        icon:"chevron-triple-left"

        id:button_6

        pos_hint:{'center_x':0.1,'center_y':0.9}

        on_press:root.manager.current='Main'

    MDRoundFlatButton:

        text:"SUBMIT"

        id:button_9

        pos_hint:{'center_x':0.5,'center_y':0.1}

        on_press:app.submit3()
        on_press:root.manager.current='Out3'


<Output1Screen>:

    

    name:'Out1'

    MDRoundFlatButton:

        text:"SHOW RESULT"

        id:button_10

        pos_hint:{'center_x':0.5,'center_y':0.5}

        on_press:app.bmi1()

    MDIconButton:

        icon:"chevron-triple-left"

        id:button_13

        pos_hint:{'center_x':0.1,'center_y':0.9}

        on_press:root.manager.current='Main'


<Output2Screen>:

    

    name:'Out2'

    MDRoundFlatButton:

        text:"SHOW RESULT"

        id:button_11

        pos_hint:{'center_x':0.5,'center_y':0.5}

        on_press:app.bmi2()

    MDIconButton:

        icon:"chevron-triple-left"

        id:button_14

        pos_hint:{'center_x':0.1,'center_y':0.9}

        on_press:root.manager.current='Main'


<Output3Screen>:

    

    name:'Out3'

    MDRoundFlatButton:

        text:"SHOW RESULT"

        id:button_12

        pos_hint:{'center_x':0.5,'center_y':0.5}

        on_press:app.bmi3()

    MDIconButton:

        icon:"chevron-triple-left"

        id:button_15

        pos_hint:{'center_x':0.1,'center_y':0.9}

        on_press:root.manager.current='Main'



    """

class MainScreen(Screen):
    pass

class FtScreen(Screen):
    pass

class CmScreen(Screen):
    pass


class MScreen(Screen):
    pass

class Output1Screen(Screen):
    pass

class Output2Screen(Screen):
    pass

class Output3Screen(Screen):
    pass


class BMI(MDApp):
    
    def build(self):
        
        self.screen=Builder.load_string(screen_helper)
                                        
        return self.screen

    def submit1(self):

        mainscreen_instance=self.screen.get_screen('Main')
        ftscreen_instance=self.screen.get_screen('Feet')

        weight=mainscreen_instance.ids.input_1.text

        height_foot=ftscreen_instance.ids.input_2.text

        height_inch=ftscreen_instance.ids.input_3.text

        if (weight=="")or(height_foot=="")or(height_inch=="")or(weight<='0')or(height_foot<='0')or(height_inch<'0'):

            dialogdisplay="WRONG INPUT"
            
        else:

            l=[]#List for input data

            l.append(weight)

            l.append('\n')

            l.append(height_foot)

            l.append('\n')

            l.append(height_inch)

            f=open("bmi.txt",'w')#file

            for i in l:

                f.write(i)

            f.close()
            
            dialogdisplay="Success!!!"

        dclose_button=MDFlatButton(text="Ok",on_release=self.closedialog)#Dialogbox closing button

        self.dialog=MDDialog(title="BMI",text=dialogdisplay,

                        size_hint=(0.7,1),

                        buttons=[dclose_button,])# creates a dialogbox

        self.dialog.open()#pops up the dialogbox on screen
        

    def submit2(self):

        mainscreen_instance=self.screen.get_screen('Main')
        cmscreen_instance=self.screen.get_screen('Cm')

        weight=mainscreen_instance.ids.input_1.text

        height=cmscreen_instance.ids.input_4.text

        if (weight=="")or(height=="")or(weight<='0')or(height<='0'):

            dialogdisplay="WRONG INPUT"
            
        else:

            l=[]#List for input data

            l.append(weight)

            l.append('\n')

            l.append(height)

            f=open("bmi.txt",'w')#file

            for i in l:

                f.write(i)

            f.close()

            dialogdisplay="Success!!!"

        dclose_button=MDFlatButton(text="Ok",on_release=self.closedialog)#Dialogbox closing button

        self.dialog=MDDialog(title="BMI",text=dialogdisplay,

                        size_hint=(0.7,1),

                        buttons=[dclose_button,])# creates a dialogbox

        self.dialog.open()#pops up the dialogbox on screen

    def submit3(self):

        mainscreen_instance=self.screen.get_screen('Main')
        mscreen_instance=self.screen.get_screen('M')

        weight=mainscreen_instance.ids.input_1.text

        height=mscreen_instance.ids.input_5.text

        if (weight=="")or(height=="")or(weight<='0')or(height<='0'):

            dialogdisplay="WRONG INPUT"
            
        else:

            l=[]#List for input data

            l.append(weight)

            l.append('\n')

            l.append(height)

            f=open("bmi.txt",'w')#file

            for i in l:

                f.write(i)

            f.close()

            dialogdisplay="Success!!!"

        dclose_button=MDFlatButton(text="Ok",on_release=self.closedialog)#Dialogbox closing button

        self.dialog=MDDialog(title="BMI",text=dialogdisplay,

                        size_hint=(0.7,1),

                        buttons=[dclose_button,])# creates a dialogbox

        self.dialog.open()#pops up the dialogbox on screen



        

    def closedialog(self,reg):#Dialogbox Closing button functionality

        self.dialog.dismiss()

    def bmi1(self):

        f=open("bmi.txt",'r')

        r=f.readlines()

        f.close()

        weight =float(r[0].strip())

        height_foot =float(r[1].strip())

        height_inch =float(r[2].strip())
        
        inch_to_feet=0.0833333*height_inch
        
        height_in_feet=height_foot+inch_to_feet
        
        height_m=0.305*height_in_feet

        bmi=weight/(height_m*height_m)

        if bmi<=18.4:
            
            a="UNDERWEIGHT"
        
        elif bmi>=18.5 and bmi<=24.9:
            
            a="NORMAL WEIGHT"
            
        elif bmi>=25.0 and bmi<=29.9:
            
            a="PRE-OBESITY/OVERWEIGHT"
            
        elif bmi>=30.0 and bmi<=34.9:
            
            a="OBESITY CLASS 1"
            
        elif bmi>=35.0 and bmi<=39.9:
            
            a="OBESITY CLASS 2"
            
        else:
            
            a="OBESITY CLASS 3"

        dialogdisplay="BMI= "+str(bmi)+"\n\nResult: "+a

        dclose_button=MDFlatButton(text="Ok",on_release=self.closedialog)#Dialogbox closing button

        self.dialog=MDDialog(title="BMI Result",text=dialogdisplay,

                        size_hint=(0.7,1),

                        buttons=[dclose_button,])# creates a dialogbox

        self.dialog.open()#pops up the dialogbox on screen


    def bmi2(self):

        f=open("bmi.txt",'r')

        r=f.readlines()

        f.close()

        weight =float(r[0].strip())

        height =float(r[1].strip())
        
        height_m=height/100

        bmi=weight/(height_m*height_m)

        if bmi<=18.4:
            
            a="UNDERWEIGHT"
        
        elif bmi>=18.5 and bmi<=24.9:
            
            a="NORMAL WEIGHT"
            
        elif bmi>=25.0 and bmi<=29.9:
            
            a="PRE-OBESITY/OVERWEIGHT"
            
        elif bmi>=30.0 and bmi<=34.9:
            
            a="OBESITY CLASS 1"
            
        elif bmi>=35.0 and bmi<=39.9:
            
            a="OBESITY CLASS 2"
            
        else:
            
            a="OBESITY CLASS 3"

        dialogdisplay="BMI= "+str(bmi)+"\n\nResult: "+a

        dclose_button=MDFlatButton(text="Ok",on_release=self.closedialog)#Dialogbox closing button

        self.dialog=MDDialog(title="BMI Result",text=dialogdisplay,

                        size_hint=(0.7,1),

                        buttons=[dclose_button,])# creates a dialogbox

        self.dialog.open()#pops up the dialogbox on screen

    
    def bmi3(self):

        f=open("bmi.txt",'r')

        r=f.readlines()

        f.close()

        weight =float(r[0].strip())

        height_m =float(r[1].strip())

        bmi=weight/(height_m*height_m)

        if bmi<=18.4:
            
            a="UNDERWEIGHT"
        
        elif bmi>=18.5 and bmi<=24.9:
            
            a="NORMAL WEIGHT"
            
        elif bmi>=25.0 and bmi<=29.9:
            
            a="PRE-OBESITY/OVERWEIGHT"
            
        elif bmi>=30.0 and bmi<=34.9:
            
            a="OBESITY CLASS 1"
            
        elif bmi>=35.0 and bmi<=39.9:
            
            a="OBESITY CLASS 2"
            
        else:
            
            a="OBESITY CLASS 3"

        dialogdisplay="BMI= "+str(bmi)+"\n\nResult: "+a

        dclose_button=MDFlatButton(text="Ok",on_release=self.closedialog)#Dialogbox closing button

        self.dialog=MDDialog(title="BMI Result",text=dialogdisplay,

                        size_hint=(0.7,1),

                        buttons=[dclose_button,])# creates a dialogbox

        self.dialog.open()#pops up the dialogbox on screen





BMI().run()

    
