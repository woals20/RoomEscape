from bangtal import *
import random
import time

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)
setGameOption(GameOption.ROOM_TITLE, False)

background = Scene('배경', 'Images/문(배경).png')

pic1 = Object('Images/문(조각1).png')
pic1.locate(background, 306, 400)
pic1.show()
pic1.where = 1
pic1.blank = False
pic1.click = 0

pic2 = Object('Images/문(조각2).png')
pic2.locate(background, 506, 400)
pic2.show()
pic2.where = 2
pic2.blank = False
pic2.click = 0

pic3 = Object('Images/문(조각3).png')
pic3.locate(background, 706, 400)
pic3.show()
pic3.where = 3
pic3.blank = False
pic3.click = 0

pic4 = Object('Images/문(조각4).png')
pic4.locate(background, 306, 200)
pic4.show()
pic4.where = 4
pic4.blank = False
pic4.click = 0

pic5 = Object('Images/문(조각5).png')
pic5.locate(background, 506, 200)
pic5.show()
pic5.where = 5
pic5.blank = False
pic5.click = 0

pic6 = Object('Images/문(조각6).png')
pic6.locate(background, 706, 200)
pic6.show()
pic6.where = 6
pic6.blank = False
pic6.click = 0

pic7 = Object('Images/문(조각7).png')
pic7.locate(background, 306, 0)
pic7.show()
pic7.where = 7
pic7.blank = False
pic7.click = 0

pic8 = Object('Images/문(조각8).png')
pic8.locate(background, 506, 0)
pic8.show()
pic8.where = 8
pic8.blank = False
pic8.click = 0

pic9 = Object('Images/문(조각9).png')
pic9.locate(background, 706, 0)
pic9.show()
pic9.where = 9
pic9.blank = False
pic9.click = 0

lst = [False, False, False, False, False, False, False, False, False]

start = Object('Images/시작.png')
start.locate(background, 570, 150)
start.setScale(0.1)
start.show()

end = Object('Images/정지.png')
end.locate(background, 1100, 50)
end.setScale(0.1)

def re_start():

    pic1 = Object('Images/문(조각1).png')
    pic1.locate(background, 306, 400)
    pic1.show()
    pic1.where = 1
    pic1.blank = False

    pic2 = Object('Images/문(조각2).png')
    pic2.locate(background, 506, 400)
    pic2.show()
    pic2.where = 2
    pic2.blank = False

    pic3 = Object('Images/문(조각3).png')
    pic3.locate(background, 706, 400)
    pic3.show()
    pic3.where = 3
    pic3.blank = False

    pic4 = Object('Images/문(조각4).png')
    pic4.locate(background, 306, 200)
    pic4.show()
    pic4.where = 4
    pic4.blank = False

    pic5 = Object('Images/문(조각5).png')
    pic5.locate(background, 506, 200)
    pic5.show()
    pic5.where = 5
    pic5.blank = False

    pic6 = Object('Images/문(조각6).png')
    pic6.locate(background, 706, 200)
    pic6.show()
    pic6.where = 6
    pic6.blank = False

    pic7 = Object('Images/문(조각7).png')
    pic7.locate(background, 306, 0)
    pic7.show()
    pic7.where = 7
    pic7.blank = False

    pic8 = Object('Images/문(조각8).png')
    pic8.locate(background, 506, 0)
    pic8.show()
    pic8.where = 8
    pic8.blank = False

    pic9 = Object('Images/문(조각9).png')
    pic9.locate(background, 706, 0)
    pic9.show()
    pic9.where = 9
    pic9.blank = False
    
    end.show()

def picture_shuffle():

    last = 0
    
    for i in range(1,20):
        
        for j in range(1,10000):
                  
            if pic1.blank == True:
                shuffle = random.randrange(1,3)
                if shuffle == 1 and last != 1:
                    if pic1.where == 2:
                        pic1.locate(background, 306, 400)
                        pic1.where = 1
                        pic2.blank = True
                        pic1.blank = False
                        last = 2
                        pic1.click += 1
                        break
                    elif pic2.where == 2:
                        pic2.locate(background, 306, 400)
                        pic2.where = 1
                        pic2.blank = True
                        pic1.blank = False
                        pic2.click += 1
                        last = 2
                        break
                    elif pic3.where == 2:
                        pic3.locate(background, 306, 400)
                        pic3.where = 1
                        pic2.blank = True
                        pic1.blank = False
                        pic3.click += 1
                        last = 2
                        break
                    elif pic4.where == 2:
                        pic4.locate(background, 306, 400)
                        pic4.where = 1
                        pic2.blank = True
                        pic1.blank = False
                        last = 2
                        pic4.click += 1
                        break
                    elif pic5.where == 2:
                        pic5.locate(background, 306, 400)
                        pic5.where = 1
                        pic2.blank = True
                        pic1.blank = False
                        pic5.click += 1
                        last = 2
                        break
                    elif pic6.where == 2:
                        pic6.locate(background, 306, 400)
                        pic6.where = 1
                        pic2.blank = True
                        pic1.blank = False
                        pic6.click +=1
                        last = 2
                        break
                    elif pic7.where == 2:
                        pic7.locate(background, 306, 400)
                        pic7.where = 1
                        pic2.blank = True
                        pic1.blank = False
                        pic7.click += 1
                        last = 2
                        break
                    elif pic8.where == 2:
                        pic8.locate(background, 306, 400)
                        pic8.where = 1
                        pic2.blank = True
                        pic1.blank = False
                        last = 2
                        pic8.click += 1
                        break
                    elif pic9.where == 2:
                        pic9.locate(background, 306, 400)
                        pic9.where = 1
                        pic2.blank = True
                        pic1.blank = False
                        last = 2
                        pic9.click += 1
                        break
                elif shuffle == 2 and last != 1:
                    if pic1.where == 4:
                        pic1.locate(background, 306, 400)
                        pic1.where = 1
                        pic4.blank = True
                        pic1.blank = False
                        last = 4
                        pic1.click += 1
                        break
                    if pic2.where == 4:
                        pic2.locate(background, 306, 400)
                        pic2.where = 1
                        pic4.blank = True
                        pic1.blank = False
                        last = 4
                        pic2.click += 1
                        break
                    if pic3.where == 4:
                        pic3.locate(background, 306, 400)
                        pic3.where = 1
                        pic4.blank = True
                        pic1.blank = False
                        last = 4
                        pic3.click += 1
                        break
                    if pic4.where == 4:
                        pic4.locate(background, 306, 400)
                        pic4.where = 1
                        pic4.blank = True
                        pic1.blank = False
                        last = 4
                        pic4.click += 1
                        break
                    if pic5.where == 4:
                        pic5.locate(background, 306, 400)
                        pic5.where = 1
                        pic4.blank = True
                        pic1.blank = False
                        last = 4
                        pic5.click += 1
                        break
                    if pic6.where == 4:
                        pic6.locate(background, 306, 400)
                        pic6.where = 1
                        pic4.blank = True
                        pic1.blank = False
                        last = 4
                        pic6.click += 1
                        break
                    if pic7.where == 4:
                        pic7.locate(background, 306, 400)
                        pic7.where = 1
                        pic4.blank = True
                        pic1.blank = False
                        last = 4
                        pic7.click += 1
                        break
                    if pic8.where == 4:
                        pic8.locate(background, 306, 400)
                        pic8.where = 1
                        pic4.blank = True
                        pic1.blank = False
                        last = 4
                        pic8.click += 1
                        break
                    if pic9.where == 4:
                        pic9.locate(background, 306, 400)
                        pic9.where = 1
                        pic4.blank = True
                        pic1.blank = False
                        last = 4
                        pic9.click += 1
                        break
            if pic2.blank == True:
                shuffle = random.randrange(1,4)
                if shuffle == 1 and last != 2:
                    if pic1.where == 1:
                        pic1.locate(background, 506, 400)
                        pic1.where = 2
                        pic1.blank = True
                        pic2.blank = False
                        last = 1
                        pic1.click += 1
                        break
                    if pic2.where == 1:
                        pic2.locate(background, 506, 400)
                        pic2.where = 2
                        pic1.blank = True
                        pic2.blank = False
                        last = 1
                        pic2.click += 1
                        break
                    if pic3.where == 1:
                        pic3.locate(background, 506, 400)
                        pic3.where = 2
                        pic1.blank = True
                        pic2.blank = False
                        last = 1
                        pic3.click += 1
                        break
                    if pic4.where == 1:
                        pic4.locate(background, 506, 400)
                        pic4.where = 2
                        pic1.blank = True
                        pic2.blank = False
                        last = 1
                        pic4.click += 1
                        break
                    if pic5.where == 1:
                        pic5.locate(background, 506, 400)
                        pic5.where = 2
                        pic1.blank = True
                        pic2.blank = False
                        last = 1
                        pic5.click += 1
                        break
                    if pic6.where == 1:
                        pic6.locate(background, 506, 400)
                        pic6.where = 2
                        pic1.blank = True
                        pic2.blank = False
                        last = 1
                        pic6.click += 1
                        break
                    if pic7.where == 1:
                        pic7.locate(background, 506, 400)
                        pic7.where = 2
                        pic1.blank = True
                        pic2.blank = False
                        last = 1
                        pic7.click += 1
                        break
                    if pic8.where == 1:
                        pic8.locate(background, 506, 400)
                        pic8.where = 2
                        pic1.blank = True
                        pic2.blank = False
                        last = 1
                        pic8.click += 1
                        break
                    if pic9.where == 1:
                        pic9.locate(background, 506, 400)
                        pic9.where = 2
                        pic1.blank = True
                        pic2.blank = False
                        last = 1
                        pic9.click += 1
                        break
                if shuffle == 2 and last != 2:
                    if pic1.where == 3:
                        pic1.locate(background, 506, 400)
                        pic1.where = 2
                        pic3.blank = True
                        pic2.blank = False
                        last = 3
                        pic1.click += 1
                        break
                    if pic2.where == 3:
                        pic2.locate(background, 506, 400)
                        pic2.where = 2
                        pic3.blank = True
                        pic2.blank = False
                        last = 3
                        pic2.click += 1
                        break
                    if pic3.where == 3:
                        pic3.locate(background, 506, 400)
                        pic3.where = 2
                        pic3.blank = True
                        pic2.blank = False
                        last = 3
                        pic3.click += 1
                        break
                    if pic4.where == 3:
                        pic4.locate(background, 506, 400)
                        pic4.where = 2
                        pic3.blank = True
                        pic2.blank = False
                        last = 3
                        pic4.click += 1
                        break
                    if pic5.where == 3:
                        pic5.locate(background, 506, 400)
                        pic5.where = 2
                        pic3.blank = True
                        pic2.blank = False
                        last = 3
                        pic5.click += 1
                        break
                    if pic6.where == 3:
                        pic6.locate(background, 506, 400)
                        pic6.where = 2
                        pic3.blank = True
                        pic2.blank = False
                        last = 3
                        pic6.click += 1
                        break
                    if pic7.where == 3:
                        pic7.locate(background, 506, 400)
                        pic7.where = 2
                        pic3.blank = True
                        pic2.blank = False
                        last = 3
                        pic7.click += 1
                        break
                    if pic8.where == 3:
                        pic8.locate(background, 506, 400)
                        pic8.where = 2
                        pic3.blank = True
                        pic2.blank = False
                        last = 3
                        pic8.click += 1
                        break
                    if pic9.where == 3:
                        pic9.locate(background, 506, 400)
                        pic9.where = 2
                        pic3.blank = True
                        pic2.blank = False
                        last = 3
                        pic9.click += 1
                        break
                if shuffle == 3 and last != 2:
                    if pic1.where == 5:
                        pic1.locate(background, 506, 400)
                        pic1.where = 2
                        pic5.blank = True
                        pic2.blank = False
                        last = 5
                        pic1.click += 1
                        break
                    if pic2.where == 5:
                        pic2.locate(background, 506, 400)
                        pic2.where = 2
                        pic5.blank = True
                        pic2.blank = False
                        last = 5
                        pic2.click += 1
                        break
                    if pic3.where == 5:
                        pic3.locate(background, 506, 400)
                        pic3.where = 2
                        pic5.blank = True
                        pic2.blank = False
                        last = 5
                        pic3.click += 1
                        break
                    if pic4.where == 5:
                        pic4.locate(background, 506, 400)
                        pic4.where = 2
                        pic5.blank = True
                        pic2.blank = False
                        last = 5
                        pic4.click += 1
                        break
                    if pic5.where == 5:
                        pic5.locate(background, 506, 400)
                        pic5.where = 2
                        pic5.blank = True
                        pic2.blank = False
                        last = 5
                        pic5.click += 1
                        break
                    if pic6.where == 5:
                        pic6.locate(background, 506, 400)
                        pic6.where = 2
                        pic5.blank = True
                        pic2.blank = False
                        last = 5
                        pic6.click += 1
                        break
                    if pic7.where == 5:
                        pic7.locate(background, 506, 400)
                        pic7.where = 2
                        pic5.blank = True
                        pic2.blank = False
                        last = 5
                        pic7.click += 1
                        break
                    if pic8.where == 5:
                        pic8.locate(background, 506, 400)
                        pic8.where = 2
                        pic5.blank = True
                        pic2.blank = False
                        last = 5
                        pic8.click += 1
                        break
                    if pic9.where == 5:
                        pic9.locate(background, 506, 400)
                        pic9.where = 2
                        pic5.blank = True
                        pic2.blank = False
                        last = 5
                        pic9.click += 1
                        break
            if pic3.blank == True:
                shuffle = random.randrange(1,3)
                if shuffle == 1 and last != 3:
                    if pic1.where == 2:
                        pic1.locate(background, 706, 400)
                        pic1.where = 3
                        pic2.blank = True
                        pic3.blank = False
                        last = 2
                        pic1.click += 1
                        break
                    elif pic2.where == 2:
                        pic2.locate(background, 706, 400)
                        pic2.where = 3
                        pic2.blank = True
                        pic3.blank = False
                        last = 2
                        pic2.click += 1
                        break
                    elif pic3.where == 2:
                        pic3.locate(background, 706, 400)
                        pic3.where = 3
                        pic2.blank = True
                        pic3.blank = False
                        last = 2
                        pic3.click += 1
                        break
                    elif pic4.where == 2:
                        pic4.locate(background, 706, 400)
                        pic4.where = 3
                        pic2.blank = True
                        pic3.blank = False
                        last = 2
                        pic4.click += 1
                        break
                    elif pic5.where == 2:
                        pic5.locate(background, 706, 400)
                        pic5.where = 3
                        pic2.blank = True
                        pic3.blank = False
                        last = 2
                        pic5.click += 1
                        break
                    elif pic6.where == 2:
                        pic6.locate(background, 706, 400)
                        pic6.where = 3
                        pic2.blank = True
                        pic3.blank = False
                        last = 2
                        pic6.click += 1
                        break
                    elif pic7.where == 2:
                        pic7.locate(background, 706, 400)
                        pic7.where = 3
                        pic2.blank = True
                        pic3.blank = False
                        last = 2
                        pic7.click += 1
                        break
                    elif pic8.where == 2:
                        pic8.locate(background, 706, 400)
                        pic8.where = 3
                        pic2.blank = True
                        pic3.blank = False
                        last = 2
                        pic8.click += 1
                        break
                    elif pic9.where == 2:
                        pic9.locate(background, 706, 400)
                        pic9.where = 3
                        pic2.blank = True
                        pic3.blank = False
                        last = 2
                        pic9.click += 1
                        break
                elif shuffle == 2and last != 3:
                    if pic1.where == 6:
                        pic1.locate(background, 706, 400)
                        pic1.where = 3
                        pic6.blank = True
                        pic3.blank = False
                        last = 6
                        pic1.click += 1
                        break
                    if pic2.where == 6:
                        pic2.locate(background, 706, 400)
                        pic2.where = 3
                        pic6.blank = True
                        pic3.blank = False
                        last = 6
                        pic2.click += 1
                        break
                    if pic3.where == 6:
                        pic3.locate(background, 706, 400)
                        pic3.where = 3
                        pic6.blank = True
                        pic3.blank = False
                        last = 6
                        pic3.click += 1
                        break
                    if pic4.where == 6:
                        pic4.locate(background, 706, 400)
                        pic4.where = 3
                        pic6.blank = True
                        pic3.blank = False
                        last = 6
                        pic4.click += 1
                        break
                    if pic5.where == 6:
                        pic5.locate(background, 706, 400)
                        pic5.where = 3
                        pic6.blank = True
                        pic3.blank = False
                        last = 6
                        pic5.click += 1
                        break
                    if pic6.where == 6:
                        pic6.locate(background, 706, 400)
                        pic6.where = 3
                        pic6.blank = True
                        pic3.blank = False
                        last = 6
                        pic6.click += 1
                        break
                    if pic7.where == 6:
                        pic7.locate(background, 706, 400)
                        pic7.where = 3
                        pic6.blank = True
                        pic3.blank = False
                        last = 6
                        pic7.click += 1
                        break
                    if pic8.where == 6:
                        pic8.locate(background, 706, 400)
                        pic8.where = 3
                        pic6.blank = True
                        pic3.blank = False
                        last = 6
                        pic8.click += 1
                        break
                    if pic9.where == 6:
                        pic9.locate(background, 706, 400)
                        pic9.where = 3
                        pic6.blank = True
                        pic3.blank = False
                        last = 6
                        pic9.click += 1
                        break
            if pic4.blank == True:
                shuffle = random.randrange(1,4)
                if shuffle == 1 and last !=4:
                    if pic1.where == 1:
                        pic1.locate(background, 306, 200)
                        pic1.where = 4
                        pic1.blank = True
                        pic4.blank = False
                        last = 1
                        pic1.click += 1
                        break
                    if pic2.where == 1:
                        pic2.locate(background, 306, 200)
                        pic2.where = 4
                        pic1.blank = True
                        pic4.blank = False
                        last = 1
                        pic2.click += 1
                        break
                    if pic3.where == 1:
                        pic3.locate(background, 306, 200)
                        pic3.where = 4
                        pic1.blank = True
                        pic4.blank = False
                        last = 1
                        pic3.click += 1
                        break
                    if pic4.where == 1:
                        pic4.locate(background, 306, 200)
                        pic4.where = 4
                        pic1.blank = True
                        pic4.blank = False
                        last = 1
                        pic4.click += 1
                        break
                    if pic5.where == 1:
                        pic5.locate(background, 306, 200)
                        pic5.where = 4
                        pic1.blank = True
                        pic4.blank = False
                        last = 1
                        pic5.click += 1
                        break
                    if pic6.where == 1:
                        pic6.locate(background, 306, 200)
                        pic6.where = 4
                        pic1.blank = True
                        pic4.blank = False
                        last = 1
                        pic6.click += 1
                        break
                    if pic7.where == 1:
                        pic7.locate(background, 306, 200)
                        pic7.where = 4
                        pic1.blank = True
                        pic4.blank = False
                        last = 1
                        pic7.click += 1
                        break
                    if pic8.where == 1:
                        pic8.locate(background, 306, 200)
                        pic8.where = 4
                        pic1.blank = True
                        pic4.blank = False
                        last = 1
                        pic8.click += 1
                        break
                    if pic9.where == 1:
                        pic9.locate(background, 306, 200)
                        pic9.where = 4
                        pic1.blank = True
                        pic4.blank = False
                        last = 1
                        pic9.click += 1
                        break
                if shuffle == 2 and last !=4:
                    if pic1.where == 5:
                        pic1.locate(background, 306, 200)
                        pic1.where = 4
                        pic5.blank = True
                        pic4.blank = False
                        last = 5
                        pic1.click += 1
                        break
                    if pic2.where == 5:
                        pic2.locate(background, 306, 200)
                        pic2.where = 4
                        pic5.blank = True
                        pic4.blank = False
                        last = 5
                        pic2.click += 1
                        break
                    if pic3.where == 5:
                        pic3.locate(background, 306, 200)
                        pic3.where = 4
                        pic5.blank = True
                        pic4.blank = False
                        last = 5
                        pic3.click += 1
                        break
                    if pic4.where == 5:
                        pic4.locate(background, 306, 200)
                        pic4.where = 4
                        pic5.blank = True
                        pic4.blank = False
                        last = 5
                        pic4.click += 1
                        break
                    if pic5.where == 5:
                        pic5.locate(background, 306, 200)
                        pic5.where = 4
                        pic5.blank = True
                        pic4.blank = False
                        last = 5
                        pic5.click += 1
                        break
                    if pic6.where == 5:
                        pic6.locate(background, 306, 200)
                        pic6.where = 4
                        pic5.blank = True
                        pic4.blank = False
                        last = 5
                        pic6.click += 1
                        break
                    if pic7.where == 5:
                        pic7.locate(background, 306, 200)
                        pic7.where = 4
                        pic5.blank = True
                        pic4.blank = False
                        last = 5
                        pic7.click += 1
                        break
                    if pic8.where == 5:
                        pic8.locate(background, 306, 200)
                        pic8.where = 4
                        pic5.blank = True
                        pic4.blank = False
                        last = 5
                        pic8.click += 1
                        break
                    if pic9.where == 5:
                        pic9.locate(background, 306, 200)
                        pic9.where = 4
                        pic5.blank = True
                        pic4.blank = False
                        last = 5
                        pic9.click += 1
                        break
                if shuffle == 3 and last !=4:
                    if pic1.where == 7:
                        pic1.locate(background, 306, 200)
                        pic1.where = 4
                        pic7.blank = True
                        pic4.blank = False
                        last = 7
                        pic1.click += 1
                        break
                    if pic2.where == 7:
                        pic2.locate(background, 306, 200)
                        pic2.where = 4
                        pic7.blank = True
                        pic4.blank = False
                        last = 7
                        pic2.click += 1
                        break
                    if pic3.where == 7:
                        pic3.locate(background, 306, 200)
                        pic3.where = 4
                        pic7.blank = True
                        pic4.blank = False
                        last = 7
                        pic3.click += 1
                        break
                    if pic4.where == 7:
                        pic4.locate(background, 306, 200)
                        pic4.where = 4
                        pic7.blank = True
                        pic4.blank = False
                        last = 7
                        pic4.click += 1
                        break
                    if pic5.where == 7:
                        pic5.locate(background, 306, 200)
                        pic5.where = 4
                        pic7.blank = True
                        pic4.blank = False
                        last = 7
                        pic5.click += 1
                        break
                    if pic6.where == 7:
                        pic6.locate(background, 306, 200)
                        pic6.where = 4
                        pic7.blank = True
                        pic4.blank = False
                        last = 7
                        pic6.click += 1
                        break
                    if pic7.where == 7:
                        pic7.locate(background, 306, 200)
                        pic7.where = 4
                        pic7.blank = True
                        pic4.blank = False
                        last = 7
                        pic7.click += 1
                        break
                    if pic8.where == 7:
                        pic8.locate(background, 306, 200)
                        pic8.where = 4
                        pic7.blank = True
                        pic4.blank = False
                        last = 7
                        pic8.click += 1
                        break
                    if pic9.where == 7:
                        pic9.locate(background, 306, 200)
                        pic9.where = 4
                        pic7.blank = True
                        pic4.blank = False
                        last = 7
                        pic9.click += 1
                        break
            if pic5.blank == True:
                shuffle = random.randrange(1,5)
                if shuffle == 1 and last != 5:
                    if pic1.where == 2:
                        pic1.locate(background, 506, 200)
                        pic1.where = 5
                        pic2.blank = True
                        pic5.blank = False
                        last = 2
                        pic1.click += 1
                        break
                    if pic2.where == 2:
                        pic2.locate(background, 506, 200)
                        pic2.where = 5
                        pic2.blank = True
                        pic5.blank = False
                        last = 2
                        pic2.click += 1
                        break
                    if pic3.where == 2:
                        pic3.locate(background, 506, 200)
                        pic3.where = 5
                        pic2.blank = True
                        pic5.blank = False
                        last = 2
                        pic3.click += 1
                        break
                    if pic4.where == 2:
                        pic4.locate(background, 506, 200)
                        pic4.where = 5
                        pic2.blank = True
                        pic5.blank = False
                        last = 2
                        pic4.click += 1
                        break
                    if pic5.where == 2:
                        pic5.locate(background, 506, 200)
                        pic5.where = 5
                        pic2.blank = True
                        pic5.blank = False
                        last = 2
                        pic5.click += 1
                        break
                    if pic6.where == 2:
                        pic6.locate(background, 506, 200)
                        pic6.where = 5
                        pic2.blank = True
                        pic5.blank = False
                        last = 2
                        pic6.click += 1
                        break
                    if pic7.where == 2:
                        pic7.locate(background, 506, 200)
                        pic7.where = 5
                        pic2.blank = True
                        pic5.blank = False
                        last = 2
                        pic7.click += 1
                        break
                    if pic8.where == 2:
                        pic8.locate(background, 506, 200)
                        pic8.where = 5
                        pic2.blank = True
                        pic5.blank = False
                        last = 2
                        pic8.click += 1
                        break
                    if pic9.where == 2:
                        pic9.locate(background, 506, 200)
                        pic9.where = 5
                        pic2.blank = True
                        pic5.blank = False
                        last = 2
                        pic9.click += 1
                        break
                if shuffle == 2 and last != 5:
                    if pic1.where == 4:
                        pic1.locate(background, 506, 200)
                        pic1.where = 5
                        pic4.blank = True
                        pic5.blank = False
                        last = 4
                        pic1.click += 1
                        break
                    if pic2.where == 4:
                        pic2.locate(background, 506, 200)
                        pic2.where = 5
                        pic4.blank = True
                        pic5.blank = False
                        last = 4
                        pic2.click += 1
                        break
                    if pic3.where == 4:
                        pic3.locate(background, 506, 200)
                        pic3.where = 5
                        pic4.blank = True
                        pic5.blank = False
                        last = 4
                        pic3.click += 1
                        break
                    if pic4.where == 4:
                        pic4.locate(background, 506, 200)
                        pic4.where = 5
                        pic4.blank = True
                        pic5.blank = False
                        last = 4
                        pic4.click += 1
                        break
                    if pic5.where == 4:
                        pic5.locate(background, 506, 200)
                        pic5.where = 5
                        pic4.blank = True
                        pic5.blank = False
                        last = 4
                        pic5.click += 1
                        break
                    if pic6.where == 4:
                        pic6.locate(background, 506, 200)
                        pic6.where = 5
                        pic4.blank = True
                        pic5.blank = False
                        last = 4
                        pic6.click += 1
                        break
                    if pic7.where == 4:
                        pic7.locate(background, 506, 200)
                        pic7.where = 5
                        pic4.blank = True
                        pic5.blank = False
                        last = 4
                        pic7.click += 1
                        break
                    if pic8.where == 4:
                        pic8.locate(background, 506, 200)
                        pic8.where = 5
                        pic4.blank = True
                        pic5.blank = False
                        last = 4
                        pic8.click += 1
                        break
                    if pic9.where == 4:
                        pic9.locate(background, 506, 200)
                        pic9.where = 5
                        pic4.blank = True
                        pic5.blank = False
                        last = 4
                        pic9.click += 1
                        break
                if shuffle == 3 and last != 5:
                    if pic1.where == 6:
                        pic1.locate(background, 506, 200)
                        pic1.where = 5
                        pic6.blank = True
                        pic5.blank = False
                        last = 6
                        pic1.click += 1
                        break
                    if pic2.where == 6:
                        pic2.locate(background, 506, 200)
                        pic2.where = 5
                        pic6.blank = True
                        pic5.blank = False
                        last = 6
                        pic2.click += 1
                        break
                    if pic3.where == 6:
                        pic3.locate(background, 506, 200)
                        pic3.where = 5
                        pic6.blank = True
                        pic5.blank = False
                        last = 6
                        pic3.click += 1
                        break
                    if pic4.where == 6:
                        pic4.locate(background, 506, 200)
                        pic4.where = 5
                        pic6.blank = True
                        pic5.blank = False
                        last = 6
                        pic4.click += 1
                        break
                    if pic5.where == 6:
                        pic5.locate(background, 506, 200)
                        pic5.where = 5
                        pic6.blank = True
                        pic5.blank = False
                        last = 6
                        pic5.click += 1
                        break
                    if pic6.where == 6:
                        pic6.locate(background, 506, 200)
                        pic6.where = 5
                        pic6.blank = True
                        pic5.blank = False
                        last = 6
                        pic6.click += 1
                        break
                    if pic7.where == 6:
                        pic7.locate(background, 506, 200)
                        pic7.where = 5
                        pic6.blank = True
                        pic5.blank = False
                        last = 6
                        pic7.click += 1
                        break
                    if pic8.where == 6:
                        pic8.locate(background, 506, 200)
                        pic8.where = 5
                        pic6.blank = True
                        pic5.blank = False
                        last = 6
                        pic8.click += 1
                        break
                    if pic9.where == 6:
                        pic9.locate(background, 506, 200)
                        pic9.where = 5
                        pic6.blank = True
                        pic5.blank = False
                        last = 6
                        pic9.click += 1
                        break
                if shuffle == 4 and last != 5:
                    if pic1.where == 8:
                        pic1.locate(background, 506, 200)
                        pic1.where = 5
                        pic8.blank = True
                        pic5.blank = False
                        last = 8
                        pic1.click += 1
                        break
                    if pic2.where == 8:
                        pic2.locate(background, 506, 200)
                        pic2.where = 5
                        pic8.blank = True
                        pic5.blank = False
                        last = 8
                        pic2.click += 1
                        break
                    if pic3.where == 8:
                        pic3.locate(background, 506, 200)
                        pic3.where = 5
                        pic8.blank = True
                        pic5.blank = False
                        last = 8
                        pic3.click += 1
                        break
                    if pic4.where == 8:
                        pic4.locate(background, 506, 200)
                        pic4.where = 5
                        pic8.blank = True
                        pic5.blank = False
                        last = 8
                        pic4.click += 1
                        break
                    if pic5.where == 8:
                        pic5.locate(background, 506, 200)
                        pic5.where = 5
                        pic8.blank = True
                        pic5.blank = False
                        last = 8
                        pic5.click += 1
                        break
                    if pic6.where == 8:
                        pic6.locate(background, 506, 200)
                        pic6.where = 5
                        pic8.blank = True
                        pic5.blank = False
                        last = 8
                        pic6.click += 1
                        break
                    if pic7.where == 8:
                        pic7.locate(background, 506, 200)
                        pic7.where = 5
                        pic8.blank = True
                        pic5.blank = False
                        last = 8
                        pic7.click += 1
                        break
                    if pic8.where == 8:
                        pic8.locate(background, 506, 200)
                        pic8.where = 5
                        pic8.blank = True
                        pic5.blank = False
                        last = 8
                        pic8.click += 1
                        break
                    if pic9.where == 8:
                        pic9.locate(background, 506, 200)
                        pic9.where = 5
                        pic8.blank = True
                        pic5.blank = False
                        last = 8
                        pic9.click += 1
                        break
            if pic6.blank == True:
                shuffle = random.randrange(1,4)
                if shuffle == 1 and last != 6:
                    if pic1.where == 3:
                        pic1.locate(background, 706, 200)
                        pic1.where = 6
                        pic3.blank = True
                        pic6.blank = False
                        last = 3
                        pic1.click += 1
                        break
                    if pic2.where == 3:
                        pic2.locate(background, 706, 200)
                        pic2.where = 6
                        pic3.blank = True
                        pic6.blank = False
                        last = 3
                        pic2.click += 1
                        break
                    if pic3.where == 3:
                        pic3.locate(background, 706, 200)
                        pic3.where = 6
                        pic3.blank = True
                        pic6.blank = False
                        last = 3
                        pic3.click += 1
                        break
                    if pic4.where == 3:
                        pic4.locate(background, 706, 200)
                        pic4.where = 6
                        pic3.blank = True
                        pic6.blank = False
                        last = 3
                        pic4.click += 1
                        break
                    if pic5.where == 3:
                        pic5.locate(background, 706, 200)
                        pic5.where = 6
                        pic3.blank = True
                        pic6.blank = False
                        last = 3
                        pic5.click += 1
                        break
                    if pic6.where == 3:
                        pic6.locate(background, 706, 200)
                        pic6.where = 6
                        pic3.blank = True
                        pic6.blank = False
                        last = 3
                        pic6.click += 1
                        break
                    if pic7.where == 3:
                        pic7.locate(background, 706, 200)
                        pic7.where = 6
                        pic3.blank = True
                        pic6.blank = False
                        last = 3
                        pic7.click += 1
                        break
                    if pic8.where == 3:
                        pic8.locate(background, 706, 200)
                        pic8.where = 6
                        pic3.blank = True
                        pic6.blank = False
                        last = 3
                        pic8.click += 1
                        break
                    if pic9.where == 3:
                        pic9.locate(background, 706, 200)
                        pic9.where = 6
                        pic3.blank = True
                        pic6.blank = False
                        last = 3
                        pic9.click += 1
                        break
                if shuffle == 2 and last != 6:
                    if pic1.where == 5:
                        pic1.locate(background, 706, 200)
                        pic1.where = 6
                        pic5.blank = True
                        pic6.blank = False
                        last = 5
                        pic1.click += 1
                        break
                    if pic2.where == 5:
                        pic2.locate(background, 706, 200)
                        pic2.where = 6
                        pic5.blank = True
                        pic6.blank = False
                        last = 5
                        pic2.click += 1
                        break
                    if pic3.where == 5:
                        pic3.locate(background, 706, 200)
                        pic3.where = 6
                        pic5.blank = True
                        pic6.blank = False
                        last = 5
                        pic3.click += 1
                        break
                    if pic4.where == 5:
                        pic4.locate(background, 706, 200)
                        pic4.where = 6
                        pic5.blank = True
                        pic6.blank = False
                        last = 5
                        pic4.click += 1
                        break
                    if pic5.where == 5:
                        pic5.locate(background, 706, 200)
                        pic5.where = 6
                        pic5.blank = True
                        pic6.blank = False
                        last = 5
                        pic5.click += 1
                        break
                    if pic6.where == 5:
                        pic6.locate(background, 706, 200)
                        pic6.where = 6
                        pic5.blank = True
                        pic6.blank = False
                        last = 5
                        pic6.click += 1
                        break
                    if pic7.where == 5:
                        pic7.locate(background, 706, 200)
                        pic7.where = 6
                        pic5.blank = True
                        pic6.blank = False
                        last = 5
                        pic7.click += 1
                        break
                    if pic8.where == 5:
                        pic8.locate(background, 706, 200)
                        pic8.where = 6
                        pic5.blank = True
                        pic6.blank = False
                        last = 5
                        pic8.click += 1
                        break
                    if pic9.where == 5:
                        pic9.locate(background, 706, 200)
                        pic9.where = 6
                        pic5.blank = True
                        pic6.blank = False
                        last = 5
                        pic9.click += 1
                        break
                if shuffle == 3 and last != 6:
                    if pic1.where == 9:
                        pic1.locate(background, 706, 200)
                        pic1.where = 6
                        pic9.blank = True
                        pic6.blank = False
                        last = 9
                        pic1.click += 1
                        break
                    if pic2.where == 9:
                        pic2.locate(background, 706, 200)
                        pic2.where = 6
                        pic9.blank = True
                        pic6.blank = False
                        last = 9
                        pic2.click += 1
                        break
                    if pic3.where == 9:
                        pic3.locate(background, 706, 200)
                        pic3.where = 6
                        pic9.blank = True
                        pic6.blank = False
                        last = 9
                        pic3.click += 1
                        break
                    if pic4.where == 9:
                        pic4.locate(background, 706, 200)
                        pic4.where = 6
                        pic9.blank = True
                        pic6.blank = False
                        last = 9
                        pic4.click += 1
                        break
                    if pic5.where == 9:
                        pic5.locate(background, 706, 200)
                        pic5.where = 6
                        pic9.blank = True
                        pic6.blank = False
                        last = 9
                        pic5.click += 1
                        break
                    if pic6.where == 9:
                        pic6.locate(background, 706, 200)
                        pic6.where = 6
                        pic9.blank = True
                        pic6.blank = False
                        last = 9
                        pic6.click += 1
                        break
                    if pic7.where == 9:
                        pic7.locate(background, 706, 200)
                        pic7.where = 6
                        pic9.blank = True
                        pic6.blank = False
                        last = 9
                        pic7.click += 1
                        break
                    if pic8.where == 9:
                        pic8.locate(background, 706, 200)
                        pic8.where = 6
                        pic9.blank = True
                        pic6.blank = False
                        last = 9
                        pic8.click += 1
                        break
                    if pic9.where == 9:
                        pic9.locate(background, 706, 200)
                        pic9.where = 6
                        pic9.blank = True
                        pic6.blank = False
                        last = 9
                        pic9.click += 1
                        break
            if pic7.blank == True:
                shuffle = random.randrange(1,3)
                if shuffle == 1 and last != 7:
                    if pic1.where == 4:
                        pic1.locate(background, 306, 0)
                        pic1.where = 7
                        pic4.blank = True
                        pic7.blank = False
                        last = 4
                        pic1.click += 1
                        break
                    if pic2.where == 4:
                        pic2.locate(background, 306, 0)
                        pic2.where = 7
                        pic4.blank = True
                        pic7.blank = False
                        last = 4
                        pic2.click += 1
                        break
                    if pic3.where == 4:
                        pic3.locate(background, 306, 0)
                        pic3.where = 7
                        pic4.blank = True
                        pic7.blank = False
                        last = 4
                        pic3.click += 1
                        break
                    if pic4.where == 4:
                        pic4.locate(background, 306, 0)
                        pic4.where = 7
                        pic4.blank = True
                        pic7.blank = False
                        last = 4
                        pic4.click += 1
                        break
                    if pic5.where == 4:
                        pic5.locate(background, 306, 0)
                        pic5.where = 7
                        pic4.blank = True
                        pic7.blank = False
                        last = 4
                        pic5.click += 1
                        break
                    if pic6.where == 4:
                        pic6.locate(background, 306, 0)
                        pic6.where = 7
                        pic4.blank = True
                        pic7.blank = False
                        last = 4
                        pic6.click += 1
                        break
                    if pic7.where == 4:
                        pic7.locate(background, 306, 0)
                        pic7.where = 7
                        pic4.blank = True
                        pic7.blank = False
                        last = 4
                        pic7.click += 1
                        break
                    if pic8.where == 4:
                        pic8.locate(background, 306, 0)
                        pic8.where = 7
                        pic4.blank = True
                        pic7.blank = False
                        last = 4
                        pic8.click += 1
                        break
                    if pic9.where == 4:
                        pic9.locate(background, 306, 0)
                        pic9.where = 7
                        pic4.blank = True
                        pic7.blank = False
                        last = 4
                        pic9.click += 1
                        break
                if shuffle == 2 and last != 7:
                    if pic1.where == 8:
                        pic1.locate(background, 306, 0)
                        pic1.where = 7
                        pic8.blank = True
                        pic7.blank = False
                        last = 8
                        pic1.click += 1
                        break
                    if pic2.where == 8:
                        pic2.locate(background, 306, 0)
                        pic2.where = 7
                        pic8.blank = True
                        pic7.blank = False
                        last = 8
                        pic2.click += 1
                        break
                    if pic3.where == 8:
                        pic3.locate(background, 306, 0)
                        pic3.where = 7
                        pic8.blank = True
                        pic7.blank = False
                        last = 8
                        pic3.click += 1
                        break
                    if pic4.where == 8:
                        pic4.locate(background, 306, 0)
                        pic4.where = 7
                        pic8.blank = True
                        pic7.blank = False
                        last = 8
                        pic4.click += 1
                        break
                    if pic5.where == 8:
                        pic5.locate(background, 306, 0)
                        pic5.where = 7
                        pic8.blank = True
                        pic7.blank = False
                        last = 8
                        pic5.click += 1
                        break
                    if pic6.where == 8:
                        pic6.locate(background, 306, 0)
                        pic6.where = 7
                        pic8.blank = True
                        pic7.blank = False
                        last = 8
                        pic6.click += 1
                        break
                    if pic7.where == 8:
                        pic7.locate(background, 306, 0)
                        pic7.where = 7
                        pic8.blank = True
                        pic7.blank = False
                        last = 8
                        pic7.click += 1
                        break
                    if pic8.where == 8:
                        pic8.locate(background, 306, 0)
                        pic8.where = 7
                        pic8.blank = True
                        pic7.blank = False
                        last = 8
                        pic8.click += 1
                        break
                    if pic9.where == 8:
                        pic9.locate(background, 306, 0)
                        pic9.where = 7
                        pic8.blank = True
                        pic7.blank = False
                        last = 8
                        pic9.click += 1
                        break
            if pic8.blank == True:
                shuffle = random.randrange(1,4)
                if shuffle == 1 and last != 8:
                    if pic1.where == 5:
                        pic1.locate(background, 506, 0)
                        pic1.where = 8
                        pic5.blank = True
                        pic8.blank = False
                        last = 5
                        pic1.click += 1
                        break
                    if pic2.where == 5:
                        pic2.locate(background, 506, 0)
                        pic2.where = 8
                        pic5.blank = True
                        pic8.blank = False
                        last = 5
                        pic2.click += 1
                        break
                    if pic3.where == 5:
                        pic3.locate(background, 506, 0)
                        pic3.where = 8
                        pic5.blank = True
                        pic8.blank = False
                        last = 5
                        pic3.click += 1
                        break
                    if pic4.where == 5:
                        pic4.locate(background, 506, 0)
                        pic4.where = 8
                        pic5.blank = True
                        pic8.blank = False
                        last = 5
                        pic4.click += 1
                        break
                    if pic5.where == 5:
                        pic5.locate(background, 506, 0)
                        pic5.where = 8
                        pic5.blank = True
                        pic8.blank = False
                        last = 5
                        pic5.click += 1
                        break
                    if pic6.where == 5:
                        pic6.locate(background, 506, 0)
                        pic6.where = 8
                        pic5.blank = True
                        pic8.blank = False
                        last = 5
                        pic6.click += 1
                        break
                    if pic7.where == 5:
                        pic7.locate(background, 506, 0)
                        pic7.where = 8
                        pic5.blank = True
                        pic8.blank = False
                        last = 5
                        pic7.click += 1
                        break
                    if pic8.where == 5:
                        pic8.locate(background, 506, 0)
                        pic8.where = 8
                        pic5.blank = True
                        pic8.blank = False
                        last = 5
                        pic8.click += 1
                        break
                    if pic9.where == 5:
                        pic9.locate(background, 506, 0)
                        pic9.where = 8
                        pic5.blank = True
                        pic8.blank = False
                        last = 5
                        pic9.click += 1
                        break
                if shuffle == 2 and last != 8:
                    if pic1.where == 7:
                        pic1.locate(background, 506, 0)
                        pic1.where = 8
                        pic7.blank = True
                        pic8.blank = False
                        last = 7
                        pic1.click += 1
                        break
                    if pic2.where == 7:
                        pic2.locate(background, 506, 0)
                        pic2.where = 8
                        pic7.blank = True
                        pic8.blank = False
                        last = 7
                        pic2.click += 1
                        break
                    if pic3.where == 7:
                        pic3.locate(background, 506, 0)
                        pic3.where = 8
                        pic7.blank = True
                        pic8.blank = False
                        last = 7
                        pic3.click += 1
                        break
                    if pic4.where == 7:
                        pic4.locate(background, 506, 0)
                        pic4.where = 8
                        pic7.blank = True
                        pic8.blank = False
                        last = 7
                        pic4.click += 1
                        break
                    if pic5.where == 7:
                        pic5.locate(background, 506, 0)
                        pic5.where = 8
                        pic7.blank = True
                        pic8.blank = False
                        last = 7
                        pic5.click += 1
                        break
                    if pic6.where == 7:
                        pic6.locate(background, 506, 0)
                        pic6.where = 8
                        pic7.blank = True
                        pic8.blank = False
                        last = 7
                        pic6.click += 1
                        break
                    if pic7.where == 7:
                        pic7.locate(background, 506, 0)
                        pic7.where = 8
                        pic7.blank = True
                        pic8.blank = False
                        last = 7
                        pic7.click += 1
                        break
                    if pic8.where == 7:
                        pic8.locate(background, 506, 0)
                        pic8.where = 8
                        pic7.blank = True
                        pic8.blank = False
                        last = 7
                        pic8.click += 1
                        break
                    if pic9.where == 7:
                        pic9.locate(background, 506, 0)
                        pic9.where = 8
                        pic7.blank = True
                        pic8.blank = False
                        last = 7
                        pic9.click += 1
                        break
                if shuffle == 3 and last != 8:
                    if pic1.where == 9:
                        pic1.locate(background, 506, 0)
                        pic1.where = 8
                        pic9.blank = True
                        pic8.blank = False
                        last = 9
                        pic1.click += 1
                        break
                    if pic2.where == 9:
                        pic2.locate(background, 506, 0)
                        pic2.where = 8
                        pic9.blank = True
                        pic8.blank = False
                        last = 9
                        pic2.click += 1
                        break
                    if pic3.where == 9:
                        pic3.locate(background, 506, 0)
                        pic3.where = 8
                        pic9.blank = True
                        pic8.blank = False
                        last = 9
                        pic3.click += 1
                        break
                    if pic4.where == 9:
                        pic4.locate(background, 506, 0)
                        pic4.where = 8
                        pic9.blank = True
                        pic8.blank = False
                        last = 9
                        pic4.click += 1
                        break
                    if pic5.where == 9:
                        pic5.locate(background, 506, 0)
                        pic5.where = 8
                        pic9.blank = True
                        pic8.blank = False
                        last = 9
                        pic5.click += 1
                        break
                    if pic6.where == 9:
                        pic6.locate(background, 506, 0)
                        pic6.where = 8
                        pic9.blank = True
                        pic8.blank = False
                        last = 9
                        pic6.click += 1
                        break
                    if pic7.where == 9:
                        pic7.locate(background, 506, 0)
                        pic7.where = 8
                        pic9.blank = True
                        pic8.blank = False
                        last = 9
                        pic7.click += 1
                        break
                    if pic8.where == 9:
                        pic8.locate(background, 506, 0)
                        pic8.where = 8
                        pic9.blank = True
                        pic8.blank = False
                        last = 9
                        pic8.click += 1
                        break
                    if pic9.where == 9:
                        pic9.locate(background, 506, 0)
                        pic9.where = 8
                        pic9.blank = True
                        pic8.blank = False
                        last = 9
                        pic9.click += 1
                        break
            if pic9.blank == True:
                shuffle = random.randrange(1,3)
                if shuffle == 1 and last != 9:
                    if pic1.where == 6:
                        pic1.locate(background, 706, 0)
                        pic1.where = 9
                        pic6.blank = True
                        pic9.blank = False
                        last = 6
                        pic1.click += 1
                        break
                    if pic2.where == 6:
                        pic2.locate(background, 706, 0)
                        pic2.where = 9
                        pic6.blank = True
                        pic9.blank = False
                        last = 6
                        pic2.click += 1
                        break
                    if pic3.where == 6:
                        pic3.locate(background, 706, 0)
                        pic3.where = 9
                        pic6.blank = True
                        pic9.blank = False
                        last = 6
                        pic3.click += 1
                        break
                    if pic4.where == 6:
                        pic4.locate(background, 706, 0)
                        pic4.where = 9
                        pic6.blank = True
                        pic9.blank = False
                        last = 6
                        pic4.click += 1
                        break
                    if pic5.where == 6:
                        pic5.locate(background, 706, 0)
                        pic5.where = 9
                        pic6.blank = True
                        pic9.blank = False
                        last = 6
                        pic5.click += 1
                        break
                    if pic6.where == 6:
                        pic6.locate(background, 706, 0)
                        pic6.where = 9
                        pic6.blank = True
                        pic9.blank = False
                        last = 6
                        pic6.click += 1
                        break
                    if pic7.where == 6:
                        pic7.locate(background, 706, 0)
                        pic7.where = 9
                        pic6.blank = True
                        pic9.blank = False
                        last = 6
                        pic7.click += 1
                        break
                    if pic8.where == 6:
                        pic8.locate(background, 706, 0)
                        pic8.where = 9
                        pic6.blank = True
                        pic9.blank = False
                        last = 6
                        pic8.click += 1
                        break
                    if pic9.where == 6:
                        pic9.locate(background, 706, 0)
                        pic9.where = 9
                        pic6.blank = True
                        pic9.blank = False
                        last = 6
                        pic9.click += 1
                        break
                if shuffle == 2 and last != 9:
                    if pic1.where == 8:
                        pic1.locate(background, 706, 0)
                        pic1.where = 9
                        pic8.blank = True
                        pic9.blank = False
                        last = 8
                        pic1.click += 1
                        break
                    if pic2.where == 8:
                        pic2.locate(background, 706, 0)
                        pic2.where = 9
                        pic8.blank = True
                        pic9.blank = False
                        last = 8
                        pic2.click += 1
                        break
                    if pic3.where == 8:
                        pic3.locate(background, 706, 0)
                        pic3.where = 9
                        pic8.blank = True
                        pic9.blank = False
                        last = 8
                        pic3.click += 1
                        break
                    if pic4.where == 8:
                        pic4.locate(background, 706, 0)
                        pic4.where = 9
                        pic8.blank = True
                        pic9.blank = False
                        last = 8
                        pic4.click += 1
                        break
                    if pic5.where == 8:
                        pic5.locate(background, 706, 0)
                        pic5.where = 9
                        pic8.blank = True
                        pic9.blank = False
                        last = 8
                        pic5.click += 1
                        break
                    if pic6.where == 8:
                        pic6.locate(background, 706, 0)
                        pic6.where = 9
                        pic8.blank = True
                        pic9.blank = False
                        last = 8
                        pic6.click += 1
                        break
                    if pic7.where == 8:
                        pic7.locate(background, 706, 0)
                        pic7.where = 9
                        pic8.blank = True
                        pic9.blank = False
                        last = 8
                        pic7.click += 1
                        break
                    if pic8.where == 8:
                        pic8.locate(background, 706, 0)
                        pic8.where = 9
                        pic8.blank = True
                        pic9.blank = False
                        last = 8
                        pic8.click += 1
                        break
                    if pic9.where == 8:
                        pic9.locate(background, 706, 0)
                        pic9.where = 9
                        pic8.blank = True
                        pic9.blank = False
                        last = 8
                        pic9.click += 1
                        break
                        
    

def start_onMouseAction(x, y, Action):
    start.hide()
    pick = random.randrange(1,9)

    if pick == pic1.where:
        if pic1.where == 1:
            pic1.blank = True
        elif pic1.where == 2:
            pic2.blank = True
        elif pic1.where == 3:
            pic3.blank = True
        elif pic1.where == 4:
            pic4.blank = True
        elif pic1.where == 5:
            pic5.blank = True
        elif pic1.where == 6:
            pic6.blank = True
        elif pic1.where == 7:
            pic7.blank = True
        elif pic1.where == 8:
            pic8.blank = True
        elif pic1.where == 9:
            pic9.blank = True
        pic1.hide()
        pic1.where = 0
        pic1.click = 1000000
    if pick == pic2.where:
        if pic2.where == 1:
            pic1.blank = True
        elif pic2.where == 2:
            pic2.blank = True
        elif pic2.where == 3:
            pic3.blank = True
        elif pic2.where == 4:
            pic4.blank = True
        elif pic2.where == 5:
            pic5.blank = True
        elif pic2.where == 6:
            pic6.blank = True
        elif pic2.where == 7:
            pic7.blank = True
        elif pic2.where == 8:
            pic8.blank = True
        elif pic2.where == 9:
            pic9.blank = True
        pic2.hide()
        pic2.where = 0
        pic2.click = 1000000
    if pick == pic3.where:
        if pic3.where == 1:
            pic1.blank = True
        elif pic3.where == 2:
            pic2.blank = True
        elif pic3.where == 3:
            pic3.blank = True
        elif pic3.where == 4:
            pic4.blank = True
        elif pic3.where == 5:
            pic5.blank = True
        elif pic3.where == 6:
            pic6.blank = True
        elif pic3.where == 7:
            pic7.blank = True
        elif pic3.where == 8:
            pic8.blank = True
        elif pic3.where == 9:
            pic9.blank = True
        pic3.hide()
        pic3.where = 0
        pic3.click = 1000000
    if pick == pic4.where:
        if pic4.where == 1:
            pic1.blank = True
        elif pic4.where == 2:
            pic2.blank = True
        elif pic4.where == 3:
            pic3.blank = True
        elif pic4.where == 4:
            pic4.blank = True
        elif pic4.where == 5:
            pic5.blank = True
        elif pic4.where == 6:
            pic6.blank = True
        elif pic4.where == 7:
            pic7.blank = True
        elif pic4.where == 8:
            pic8.blank = True
        elif pic4.where == 9:
            pic9.blank = True
        pic4.hide()
        pic4.where = 0
        pic4.click = 1000000
    if pick == pic5.where:
        if pic5.where == 1:
            pic1.blank = True
        elif pic5.where == 2:
            pic2.blank = True
        elif pic5.where == 3:
            pic3.blank = True
        elif pic5.where == 4:
            pic4.blank = True
        elif pic5.where == 5:
            pic5.blank = True
        elif pic5.where == 6:
            pic6.blank = True
        elif pic5.where == 7:
            pic7.blank = True
        elif pic5.where == 8:
            pic8.blank = True
        elif pic5.where == 9:
            pic9.blank = True
        pic5.hide()
        pic5.where = 0
        pic5.click = 1000000
    if pick == pic6.where:
        if pic6.where == 1:
            pic1.blank = True
        elif pic6.where == 2:
            pic2.blank = True
        elif pic6.where == 3:
            pic3.blank = True
        elif pic6.where == 4:
            pic4.blank = True
        elif pic6.where == 5:
            pic5.blank = True
        elif pic6.where == 6:
            pic6.blank = True
        elif pic6.where == 7:
            pic7.blank = True
        elif pic6.where == 8:
            pic8.blank = True
        elif pic6.where == 9:
            pic9.blank = True
        pic6.hide()
        pic6.where = 0
        pic6.click = 1000000
    if pick == pic7.where:
        if pic7.where == 1:
            pic1.blank = True
        elif pic7.where == 2:
            pic2.blank = True
        elif pic7.where == 3:
            pic3.blank = True
        elif pic7.where == 4:
            pic4.blank = True
        elif pic7.where == 5:
            pic5.blank = True
        elif pic7.where == 6:
            pic6.blank = True
        elif pic7.where == 7:
            pic7.blank = True
        elif pic7.where == 8:
            pic8.blank = True
        elif pic7.where == 9:
            pic9.blank = True
        pic7.hide()
        pic7.where = 0
        pic7.click = 1000000
    if pick == pic8.where:
        if pic8.where == 1:
            pic1.blank = True
        elif pic8.where == 2:
            pic2.blank = True
        elif pic8.where == 3:
            pic3.blank = True
        elif pic8.where == 4:
            pic4.blank = True
        elif pic8.where == 5:
            pic5.blank = True
        elif pic8.where == 6:
            pic6.blank = True
        elif pic8.where == 7:
            pic7.blank = True
        elif pic8.where == 8:
            pic8.blank = True
        elif pic8.where == 9:
            pic9.blank = True
        pic8.hide()
        pic8.where = 0
        pic8.click = 1000000
    if pick == pic9.where:
        if pic9.where == 1:
            pic1.blank = True
        elif pic9.where == 2:
            pic2.blank = True
        elif pic9.where == 3:
            pic3.blank = True
        elif pic9.where == 4:
            pic4.blank = True
        elif pic9.where == 5:
            pic5.blank = True
        elif pic9.where == 6:
            pic6.blank = True
        elif pic9.where == 7:
            pic7.blank = True
        elif pic9.where == 8:
            pic8.blank = True
        elif pic9.where == 9:
            pic9.blank = True
        pic9.hide()
        pic9.where = 0
        pic9.click = 1000000

   

    picture_shuffle()


def pic1_onMouseAction(x, y, Action):
    if pic1.where == 1:
        if pic2.blank:
            pic1.locate(background, 506, 400)
            pic1.where = 2
            pic1.blank = True
            pic2.blank = False
        elif pic4.blank:
            pic1.locate(background, 306, 200)
            pic1.where = 4
            pic1.blank = True
            pic4.blank = False
    elif pic1.where == 2:
        if pic1.blank:
            pic1.locate(background, 306, 400)
            pic1.where = 1
            pic2.blank = True
            pic1.blank = False
        elif pic3.blank:
            pic1.locate(background, 706, 400)
            pic1.where = 3
            pic2.blank = True
            pic3.blank = False
        elif pic5.blank:
            pic1.locate(background, 506, 200)
            pic1.where = 5
            pic2.blank = True
            pic5.blank = False
    elif pic1.where == 3:
        if pic2.blank:
            pic1.locate(background, 506, 400)
            pic1.where = 2
            pic3.blank = True
            pic2.blank = False
        elif pic6.blank:
            pic1.locate(background, 706, 200)
            pic1.where = 6
            pic3.blank = True
            pic6.blank = False
    elif pic1.where == 4:
        if pic1.blank:
            pic1.locate(background, 306, 400)
            pic1.where = 1
            pic4.blank = True
            pic1.blank = False
        elif pic5.blank:
            pic1.locate(background, 506, 200)
            pic1.where = 5
            pic4.blank = True
            pic5.blank = False
        elif pic7.blank:
            pic1.locate(background, 306, 0)
            pic1.where = 7
            pic4.blank = True
            pic7.blank = False
    elif pic1.where == 5:
        if pic2.blank:
            pic1.locate(background, 506, 400)
            pic1.where = 2
            pic5.blank = True
            pic2.blank = False
        elif pic4.blank:
            pic1.locate(background, 306, 200)
            pic1.where = 4
            pic5.blank = True
            pic4.blank = False
        elif pic6.blank:
            pic1.locate(background, 706, 200)
            pic1.where = 6
            pic5.blank = True
            pic6.blank = False
        elif pic8.blank:
            pic1.locate(background, 506, 0)
            pic1.where = 8
            pic5.blank = True
            pic8.blank = False
    elif pic1.where == 6:
        if pic3.blank:
            pic1.locate(background, 706, 400)
            pic1.where = 3
            pic6.blank = True
            pic3.blank = False
        elif pic5.blank:
            pic1.locate(background, 506, 200)
            pic1.where = 5
            pic6.blank = True
            pic5.blank = False
        elif pic9.blank:
            pic1.locate(background, 706, 0)
            pic1.where = 9
            pic6.blank = True
            pic9.blank = False
    elif pic1.where == 7:
        if pic4.blank:
            pic1.locate(background, 306, 200)
            pic1.where = 4
            pic7.blank = True
            pic4.blank = False
        elif pic8.blank:
            pic1.locate(background, 506, 0)
            pic1.where = 8
            pic7.blank = True
            pic8.blank = False
    elif pic1.where == 8:
        if pic5.blank:
            pic1.locate(background, 506, 200)
            pic1.where = 5
            pic8.blank = True
            pic5.blank = False
        elif pic7.blank:
            pic1.locate(background, 306, 0)
            pic1.where = 7
            pic8.blank = True
            pic7.blank = False
        elif pic9.blank:
            pic1.locate(background, 706, 0)
            pic1.where = 9
            pic8.blank = True
            pic9.blank = False
    elif pic1.where == 9:
        if pic6.blank:
            pic1.locate(background, 706, 200)
            pic1.where = 6
            pic9.blank = True
            pic6.blank = False
        elif pic8.blank:
            pic1.locate(background, 506, 0)
            pic1.where = 8
            pic9.blank = True
            pic8.blank = False

    if pic1.where == 1 or pic1.where == 0:
        if pic2.where == 2 or pic2.where == 0:
            if pic3.where == 3 or pic3.where == 0:
                if pic4.where == 4 or pic4.where == 0:
                    if pic5.where == 5 or pic5.where == 0:
                        if pic6.where == 6 or pic6.where == 0:
                            if pic7.where == 7 or pic7.where == 0:
                                if pic8.where == 8 or pic8.where == 0:
                                    if pic9.where == 9 or pic9.where == 0:
                                        pic1.hide()
                                        pic2.hide()
                                        pic3.hide()
                                        pic4.hide()
                                        pic5.hide()
                                        pic6.hide()
                                        pic7.hide()
                                        pic8.hide()
                                        pic9.hide()
                                        re_start()
                                        start.show()
        

pic1.onMouseAction = pic1_onMouseAction

def pic2_onMouseAction(x, y, Action):
    if pic2.where == 1:
        if pic2.blank:
            pic2.locate(background, 506, 400)
            pic2.where = 2
            pic1.blank = True
            pic2.blank = False
        elif pic4.blank:
            pic2.locate(background, 306, 200)
            pic2.where = 4
            pic1.blank = True
            pic4.blank = False
    elif pic2.where == 2:
        if pic1.blank:
            pic2.locate(background, 306, 400)
            pic2.where = 1
            pic2.blank = True
            pic1.blank = False
        elif pic3.blank:
            pic2.locate(background, 706, 400)
            pic2.where = 3
            pic2.blank = True
            pic3.blank = False
        elif pic5.blank:
            pic2.locate(background, 506, 200)
            pic2.where = 5
            pic2.blank = True
            pic5.blank = False
    elif pic2.where == 3:
        if pic2.blank:
            pic2.locate(background, 506, 400)
            pic2.where = 2
            pic3.blank = True
            pic2.blank = False
        elif pic6.blank:
            pic2.locate(background, 706, 200)
            pic2.where = 6
            pic3.blank = True
            pic6.blank = False
    elif pic2.where == 4:
        if pic1.blank:
            pic2.locate(background, 306, 400)
            pic2.where = 1
            pic4.blank = True
            pic1.blank = False
        elif pic5.blank:
            pic2.locate(background, 506, 200)
            pic2.where = 5
            pic4.blank = True
            pic5.blank = False
        elif pic7.blank:
            pic2.locate(background, 306, 0)
            pic2.where = 7
            pic4.blank = True
            pic7.blank = False
    elif pic2.where == 5:
        if pic2.blank:
            pic2.locate(background, 506, 400)
            pic2.where = 2
            pic5.blank = True
            pic2.blank = False
        elif pic4.blank:
            pic2.locate(background, 306, 200)
            pic2.where = 4
            pic5.blank = True
            pic4.blank = False
        elif pic6.blank:
            pic2.locate(background, 706, 200)
            pic2.where = 6
            pic5.blank = True
            pic6.blank = False
        elif pic8.blank:
            pic2.locate(background, 506, 0)
            pic2.where = 8
            pic5.blank = True
            pic8.blank = False
    elif pic2.where == 6:
        if pic3.blank:
            pic2.locate(background, 706, 400)
            pic2.where = 3
            pic6.blank = True
            pic3.blank = False
        elif pic5.blank:
            pic2.locate(background, 506, 200)
            pic2.where = 5
            pic6.blank = True
            pic5.blank = False
        elif pic9.blank:
            pic2.locate(background, 706, 0)
            pic2.where = 9
            pic6.blank = True
            pic9.blank = False
    elif pic2.where == 7:
        if pic4.blank:
            pic2.locate(background, 306, 200)
            pic2.where = 4
            pic7.blank = True
            pic4.blank = False
        elif pic8.blank:
            pic2.locate(background, 506, 0)
            pic2.where = 8
            pic7.blank = True
            pic8.blank = False
    elif pic2.where == 8:
        if pic5.blank:
            pic2.locate(background, 506, 200)
            pic2.where = 5
            pic8.blank = True
            pic5.blank = False
        elif pic7.blank:
            pic2.locate(background, 306, 0)
            pic2.where = 7
            pic8.blank = True
            pic7.blank = False
        elif pic9.blank:
            pic2.locate(background, 706, 0)
            pic2.where = 9
            pic8.blank = True
            pic9.blank = False
    elif pic2.where == 9:
        if pic6.blank:
            pic2.locate(background, 706, 200)
            pic2.where = 6
            pic9.blank = True
            pic6.blank = False
        elif pic8.blank:
            pic2.locate(background, 506, 0)
            pic2.where = 8
            pic9.blank = True
            pic8.blank = False

    if pic1.where == 1 or pic1.where == 0:
        if pic2.where == 2 or pic2.where == 0:
            if pic3.where == 3 or pic3.where == 0:
                if pic4.where == 4 or pic4.where == 0:
                    if pic5.where == 5 or pic5.where == 0:
                        if pic6.where == 6 or pic6.where == 0:
                            if pic7.where == 7 or pic7.where == 0:
                                if pic8.where == 8 or pic8.where == 0:
                                    if pic9.where == 9 or pic9.where == 0:
                                        pic1.hide()
                                        pic2.hide()
                                        pic3.hide()
                                        pic4.hide()
                                        pic5.hide()
                                        pic6.hide()
                                        pic7.hide()
                                        pic8.hide()
                                        pic9.hide()
                                        re_start()
                                        start.show()
        

pic2.onMouseAction = pic2_onMouseAction

def pic3_onMouseAction(x, y, Action):
    if pic3.where == 1:
        if pic2.blank:
            pic3.locate(background, 506, 400)
            pic3.where = 2
            pic1.blank = True
            pic2.blank = False
        elif pic4.blank:
            pic3.locate(background, 306, 200)
            pic3.where = 4
            pic1.blank = True
            pic4.blank = False
    elif pic3.where == 2:
        if pic1.blank:
            pic3.locate(background, 306, 400)
            pic3.where = 1
            pic2.blank = True
            pic1.blank = False
        elif pic3.blank:
            pic3.locate(background, 706, 400)
            pic3.where = 3
            pic2.blank = True
            pic3.blank = False
        elif pic5.blank:
            pic3.locate(background, 506, 200)
            pic3.where = 5
            pic2.blank = True
            pic5.blank = False
    elif pic3.where == 3:
        if pic2.blank:
            pic3.locate(background, 506, 400)
            pic3.where = 2
            pic3.blank = True
            pic2.blank = False
        elif pic6.blank:
            pic3.locate(background, 706, 200)
            pic3.where = 6
            pic3.blank = True
            pic6.blank = False
    elif pic3.where == 4:
        if pic1.blank:
            pic3.locate(background, 306, 400)
            pic3.where = 1
            pic4.blank = True
            pic1.blank = False
        elif pic5.blank:
            pic3.locate(background, 506, 200)
            pic3.where = 5
            pic4.blank = True
            pic5.blank = False
        elif pic7.blank:
            pic3.locate(background, 306, 0)
            pic3.where = 7
            pic4.blank = True
            pic7.blank = False
    elif pic3.where == 5:
        if pic2.blank:
            pic3.locate(background, 506, 400)
            pic3.where = 2
            pic5.blank = True
            pic2.blank = False
        elif pic4.blank:
            pic3.locate(background, 306, 200)
            pic3.where = 4
            pic5.blank = True
            pic4.blank = False
        elif pic6.blank:
            pic3.locate(background, 706, 200)
            pic3.where = 6
            pic5.blank = True
            pic6.blank = False
        elif pic8.blank:
            pic3.locate(background, 506, 0)
            pic3.where = 8
            pic5.blank = True
            pic8.blank = False
    elif pic3.where == 6:
        if pic3.blank:
            pic3.locate(background, 706, 400)
            pic3.where = 3
            pic6.blank = True
            pic3.blank = False
        elif pic5.blank:
            pic3.locate(background, 506, 200)
            pic3.where = 5
            pic6.blank = True
            pic5.blank = False
        elif pic9.blank:
            pic3.locate(background, 706, 0)
            pic3.where = 9
            pic6.blank = True
            pic9.blank = False
    elif pic3.where == 7:
        if pic4.blank:
            pic3.locate(background, 306, 200)
            pic3.where = 4
            pic7.blank = True
            pic4.blank = False
        elif pic8.blank:
            pic3.locate(background, 506, 0)
            pic3.where = 8
            pic7.blank = True
            pic8.blank = False
    elif pic3.where == 8:
        if pic5.blank:
            pic3.locate(background, 506, 200)
            pic3.where = 5
            pic8.blank = True
            pic5.blank = False
        elif pic7.blank:
            pic3.locate(background, 306, 0)
            pic3.where = 7
            pic8.blank = True
            pic7.blank = False
        elif pic9.blank:
            pic3.locate(background, 706, 0)
            pic3.where = 9
            pic8.blank = True
            pic9.blank = False
    elif pic3.where == 9:
        if pic6.blank:
            pic3.locate(background, 706, 200)
            pic3.where = 6
            pic9.blank = True
            pic6.blank = False
        elif pic8.blank:
            pic3.locate(background, 506, 0)
            pic3.where = 8
            pic9.blank = True
            pic8.blank = False

    if pic1.where == 1 or pic1.where == 0:
        if pic2.where == 2 or pic2.where == 0:
            if pic3.where == 3 or pic3.where == 0:
                if pic4.where == 4 or pic4.where == 0:
                    if pic5.where == 5 or pic5.where == 0:
                        if pic6.where == 6 or pic6.where == 0:
                            if pic7.where == 7 or pic7.where == 0:
                                if pic8.where == 8 or pic8.where == 0:
                                    if pic9.where == 9 or pic9.where == 0:
                                        pic1.hide()
                                        pic2.hide()
                                        pic3.hide()
                                        pic4.hide()
                                        pic5.hide()
                                        pic6.hide()
                                        pic7.hide()
                                        pic8.hide()
                                        pic9.hide()
                                        re_start()
                                        start.show()
        

pic3.onMouseAction = pic3_onMouseAction

def pic4_onMouseAction(x, y, Action):
    if pic4.where == 1:
        if pic2.blank:
            pic4.locate(background, 506, 400)
            pic4.where = 2
            pic1.blank = True
            pic2.blank = False
        elif pic4.blank:
            pic4.locate(background, 306, 200)
            pic4.where = 4
            pic1.blank = True
            pic4.blank = False
    elif pic4.where == 2:
        if pic1.blank:
            pic4.locate(background, 306, 400)
            pic4.where = 1
            pic2.blank = True
            pic1.blank = False
        elif pic3.blank:
            pic4.locate(background, 706, 400)
            pic4.where = 3
            pic2.blank = True
            pic3.blank = False
        elif pic5.blank:
            pic4.locate(background, 506, 200)
            pic4.where = 5
            pic2.blank = True
            pic5.blank = False
    elif pic4.where == 3:
        if pic2.blank:
            pic4.locate(background, 506, 400)
            pic4.where = 2
            pic3.blank = True
            pic2.blank = False
        elif pic6.blank:
            pic4.locate(background, 706, 200)
            pic4.where = 6
            pic3.blank = True
            pic6.blank = False
    elif pic4.where == 4:
        if pic1.blank:
            pic4.locate(background, 306, 400)
            pic4.where = 1
            pic4.blank = True
            pic1.blank = False
        elif pic5.blank:
            pic4.locate(background, 506, 200)
            pic4.where = 5
            pic4.blank = True
            pic5.blank = False
        elif pic7.blank:
            pic4.locate(background, 306, 0)
            pic4.where = 7
            pic4.blank = True
            pic7.blank = False
    elif pic4.where == 5:
        if pic2.blank:
            pic4.locate(background, 506, 400)
            pic4.where = 2
            pic5.blank = True
            pic2.blank = False
        elif pic4.blank:
            pic4.locate(background, 306, 200)
            pic4.where = 4
            pic5.blank = True
            pic4.blank = False
        elif pic6.blank:
            pic4.locate(background, 706, 200)
            pic4.where = 6
            pic5.blank = True
            pic6.blank = False
        elif pic8.blank:
            pic4.locate(background, 506, 0)
            pic4.where = 8
            pic5.blank = True
            pic8.blank = False
    elif pic4.where == 6:
        if pic3.blank:
            pic4.locate(background, 706, 400)
            pic4.where = 3
            pic6.blank = True
            pic3.blank = False
        elif pic5.blank:
            pic4.locate(background, 506, 200)
            pic4.where = 5
            pic6.blank = True
            pic5.blank = False
        elif pic9.blank:
            pic4.locate(background, 706, 0)
            pic4.where = 9
            pic6.blank = True
            pic9.blank = False
    elif pic4.where == 7:
        if pic4.blank:
            pic4.locate(background, 306, 200)
            pic4.where = 4
            pic7.blank = True
            pic4.blank = False
        elif pic8.blank:
            pic4.locate(background, 506, 0)
            pic4.where = 8
            pic7.blank = True
            pic8.blank = False
    elif pic4.where == 8:
        if pic5.blank:
            pic4.locate(background, 506, 200)
            pic4.where = 5
            pic8.blank = True
            pic5.blank = False
        elif pic7.blank:
            pic4.locate(background, 306, 0)
            pic4.where = 7
            pic8.blank = True
            pic7.blank = False
        elif pic9.blank:
            pic4.locate(background, 706, 0)
            pic4.where = 9
            pic8.blank = True
            pic9.blank = False
    elif pic4.where == 9:
        if pic6.blank:
            pic4.locate(background, 706, 200)
            pic4.where = 6
            pic9.blank = True
            pic6.blank = False
        elif pic8.blank:
            pic4.locate(background, 506, 0)
            pic4.where = 8
            pic9.blank = True
            pic8.blank = False

    if pic1.where == 1 or pic1.where == 0:
        if pic2.where == 2 or pic2.where == 0:
            if pic3.where == 3 or pic3.where == 0:
                if pic4.where == 4 or pic4.where == 0:
                    if pic5.where == 5 or pic5.where == 0:
                        if pic6.where == 6 or pic6.where == 0:
                            if pic7.where == 7 or pic7.where == 0:
                                if pic8.where == 8 or pic8.where == 0:
                                    if pic9.where == 9 or pic9.where == 0:
                                        pic1.hide()
                                        pic2.hide()
                                        pic3.hide()
                                        pic4.hide()
                                        pic5.hide()
                                        pic6.hide()
                                        pic7.hide()
                                        pic8.hide()
                                        pic9.hide()
                                        re_start()
                                        start.show()
        

pic4.onMouseAction = pic4_onMouseAction

def pic5_onMouseAction(x, y, Action):
    if pic5.where == 1:
        if pic2.blank:
            pic5.locate(background, 506, 400)
            pic5.where = 2
            pic1.blank = True
            pic2.blank = False
        elif pic4.blank:
            pic5.locate(background, 306, 200)
            pic5.where = 4
            pic1.blank = True
            pic4.blank = False
    elif pic5.where == 2:
        if pic1.blank:
            pic5.locate(background, 306, 400)
            pic5.where = 1
            pic2.blank = True
            pic1.blank = False
        elif pic3.blank:
            pic5.locate(background, 706, 400)
            pic5.where = 3
            pic2.blank = True
            pic3.blank = False
        elif pic5.blank:
            pic5.locate(background, 506, 200)
            pic5.where = 5
            pic2.blank = True
            pic5.blank = False
    elif pic5.where == 3:
        if pic2.blank:
            pic5.locate(background, 506, 400)
            pic5.where = 2
            pic3.blank = True
            pic2.blank = False
        elif pic6.blank:
            pic5.locate(background, 706, 200)
            pic5.where = 6
            pic3.blank = True
            pic6.blank = False
    elif pic5.where == 4:
        if pic1.blank:
            pic5.locate(background, 306, 400)
            pic5.where = 1
            pic4.blank = True
            pic1.blank = False
        elif pic5.blank:
            pic5.locate(background, 506, 200)
            pic5.where = 5
            pic4.blank = True
            pic5.blank = False
        elif pic7.blank:
            pic5.locate(background, 306, 0)
            pic5.where = 7
            pic4.blank = True
            pic7.blank = False
    elif pic5.where == 5:
        if pic2.blank:
            pic5.locate(background, 506, 400)
            pic5.where = 2
            pic5.blank = True
            pic2.blank = False
        elif pic4.blank:
            pic5.locate(background, 306, 200)
            pic5.where = 4
            pic5.blank = True
            pic4.blank = False
        elif pic6.blank:
            pic5.locate(background, 706, 200)
            pic5.where = 6
            pic5.blank = True
            pic6.blank = False
        elif pic8.blank:
            pic5.locate(background, 506, 0)
            pic5.where = 8
            pic5.blank = True
            pic8.blank = False
    elif pic5.where == 6:
        if pic3.blank:
            pic5.locate(background, 706, 400)
            pic5.where = 3
            pic6.blank = True
            pic3.blank = False
        elif pic5.blank:
            pic5.locate(background, 506, 200)
            pic5.where = 5
            pic6.blank = True
            pic5.blank = False
        elif pic9.blank:
            pic5.locate(background, 706, 0)
            pic5.where = 9
            pic6.blank = True
            pic9.blank = False
    elif pic5.where == 7:
        if pic4.blank:
            pic5.locate(background, 306, 200)
            pic5.where = 4
            pic7.blank = True
            pic4.blank = False
        elif pic8.blank:
            pic5.locate(background, 506, 0)
            pic5.where = 8
            pic7.blank = True
            pic8.blank = False
    elif pic5.where == 8:
        if pic5.blank:
            pic5.locate(background, 506, 200)
            pic5.where = 5
            pic8.blank = True
            pic5.blank = False
        elif pic7.blank:
            pic5.locate(background, 306, 0)
            pic5.where = 7
            pic8.blank = True
            pic7.blank = False
        elif pic9.blank:
            pic5.locate(background, 706, 0)
            pic5.where = 9
            pic8.blank = True
            pic9.blank = False
    elif pic5.where == 9:
        if pic6.blank:
            pic5.locate(background, 706, 200)
            pic5.where = 6
            pic9.blank = True
            pic6.blank = False
        elif pic8.blank:
            pic5.locate(background, 506, 0)
            pic5.where = 8
            pic9.blank = True
            pic8.blank = False

    if pic1.where == 1 or pic1.where == 0:
        if pic2.where == 2 or pic2.where == 0:
            if pic3.where == 3 or pic3.where == 0:
                if pic4.where == 4 or pic4.where == 0:
                    if pic5.where == 5 or pic5.where == 0:
                        if pic6.where == 6 or pic6.where == 0:
                            if pic7.where == 7 or pic7.where == 0:
                                if pic8.where == 8 or pic8.where == 0:
                                    if pic9.where == 9 or pic9.where == 0:
                                        pic1.hide()
                                        pic2.hide()
                                        pic3.hide()
                                        pic4.hide()
                                        pic5.hide()
                                        pic6.hide()
                                        pic7.hide()
                                        pic8.hide()
                                        pic9.hide()
                                        re_start()
                                        start.show()
        

pic5.onMouseAction = pic5_onMouseAction

def pic6_onMouseAction(x, y, Action):
    if pic6.where == 1:
        if pic2.blank:
            pic6.locate(background, 506, 400)
            pic6.where = 2
            pic1.blank = True
            pic2.blank = False
        elif pic4.blank:
            pic6.locate(background, 306, 200)
            pic6.where = 4
            pic1.blank = True
            pic4.blank = False
    elif pic6.where == 2:
        if pic1.blank:
            pic6.locate(background, 306, 400)
            pic6.where = 1
            pic2.blank = True
            pic1.blank = False
        elif pic3.blank:
            pic6.locate(background, 706, 400)
            pic6.where = 3
            pic2.blank = True
            pic3.blank = False
        elif pic5.blank:
            pic6.locate(background, 506, 200)
            pic6.where = 5
            pic2.blank = True
            pic5.blank = False
    elif pic6.where == 3:
        if pic2.blank:
            pic6.locate(background, 506, 400)
            pic6.where = 2
            pic3.blank = True
            pic2.blank = False
        elif pic6.blank:
            pic6.locate(background, 706, 200)
            pic6.where = 6
            pic3.blank = True
            pic6.blank = False
    elif pic6.where == 4:
        if pic1.blank:
            pic6.locate(background, 306, 400)
            pic6.where = 1
            pic4.blank = True
            pic1.blank = False
        elif pic5.blank:
            pic6.locate(background, 506, 200)
            pic6.where = 5
            pic4.blank = True
            pic5.blank = False
        elif pic7.blank:
            pic6.locate(background, 306, 0)
            pic6.where = 7
            pic4.blank = True
            pic7.blank = False
    elif pic6.where == 5:
        if pic2.blank:
            pic6.locate(background, 506, 400)
            pic6.where = 2
            pic5.blank = True
            pic2.blank = False
        elif pic4.blank:
            pic6.locate(background, 306, 200)
            pic6.where = 4
            pic5.blank = True
            pic4.blank = False
        elif pic6.blank:
            pic6.locate(background, 706, 200)
            pic6.where = 6
            pic5.blank = True
            pic6.blank = False
        elif pic8.blank:
            pic6.locate(background, 506, 0)
            pic6.where = 8
            pic5.blank = True
            pic8.blank = False
    elif pic6.where == 6:
        if pic3.blank:
            pic6.locate(background, 706, 400)
            pic6.where = 3
            pic6.blank = True
            pic3.blank = False
        elif pic5.blank:
            pic6.locate(background, 506, 200)
            pic6.where = 5
            pic6.blank = True
            pic5.blank = False
        elif pic9.blank:
            pic6.locate(background, 706, 0)
            pic6.where = 9
            pic6.blank = True
            pic9.blank = False
    elif pic6.where == 7:
        if pic4.blank:
            pic6.locate(background, 306, 200)
            pic6.where = 4
            pic7.blank = True
            pic4.blank = False
        elif pic8.blank:
            pic6.locate(background, 506, 0)
            pic6.where = 8
            pic7.blank = True
            pic8.blank = False
    elif pic6.where == 8:
        if pic5.blank:
            pic6.locate(background, 506, 200)
            pic6.where = 5
            pic8.blank = True
            pic5.blank = False
        elif pic7.blank:
            pic6.locate(background, 306, 0)
            pic6.where = 7
            pic8.blank = True
            pic7.blank = False
        elif pic9.blank:
            pic6.locate(background, 706, 0)
            pic6.where = 9
            pic8.blank = True
            pic9.blank = False
    elif pic6.where == 9:
        if pic6.blank:
            pic6.locate(background, 706, 200)
            pic6.where = 6
            pic9.blank = True
            pic6.blank = False
        elif pic8.blank:
            pic6.locate(background, 506, 0)
            pic6.where = 8
            pic9.blank = True
            pic8.blank = False

    if pic1.where == 1 or pic1.where == 0:
        if pic2.where == 2 or pic2.where == 0:
            if pic3.where == 3 or pic3.where == 0:
                if pic4.where == 4 or pic4.where == 0:
                    if pic5.where == 5 or pic5.where == 0:
                        if pic6.where == 6 or pic6.where == 0:
                            if pic7.where == 7 or pic7.where == 0:
                                if pic8.where == 8 or pic8.where == 0:
                                    if pic9.where == 9 or pic9.where == 0:
                                        pic1.hide()
                                        pic2.hide()
                                        pic3.hide()
                                        pic4.hide()
                                        pic5.hide()
                                        pic6.hide()
                                        pic7.hide()
                                        pic8.hide()
                                        pic9.hide()
                                        re_start()
                                        start.show()
        

pic6.onMouseAction = pic6_onMouseAction

def pic7_onMouseAction(x, y, Action):
    if pic7.where == 1:
        if pic2.blank:
            pic7.locate(background, 506, 400)
            pic7.where = 2
            pic1.blank = True
            pic2.blank = False
        elif pic4.blank:
            pic7.locate(background, 306, 200)
            pic7.where = 4
            pic1.blank = True
            pic4.blank = False
    elif pic7.where == 2:
        if pic1.blank:
            pic7.locate(background, 306, 400)
            pic7.where = 1
            pic2.blank = True
            pic1.blank = False
        elif pic3.blank:
            pic7.locate(background, 706, 400)
            pic7.where = 3
            pic2.blank = True
            pic3.blank = False
        elif pic5.blank:
            pic7.locate(background, 506, 200)
            pic7.where = 5
            pic2.blank = True
            pic5.blank = False
    elif pic7.where == 3:
        if pic2.blank:
            pic7.locate(background, 506, 400)
            pic7.where = 2
            pic3.blank = True
            pic2.blank = False
        elif pic6.blank:
            pic7.locate(background, 706, 200)
            pic7.where = 6
            pic3.blank = True
            pic6.blank = False
    elif pic7.where == 4:
        if pic1.blank:
            pic7.locate(background, 306, 400)
            pic7.where = 1
            pic4.blank = True
            pic1.blank = False
        elif pic5.blank:
            pic7.locate(background, 506, 200)
            pic7.where = 5
            pic4.blank = True
            pic5.blank = False
        elif pic7.blank:
            pic7.locate(background, 306, 0)
            pic7.where = 7
            pic4.blank = True
            pic7.blank = False
    elif pic7.where == 5:
        if pic2.blank:
            pic7.locate(background, 506, 400)
            pic7.where = 2
            pic5.blank = True
            pic2.blank = False
        elif pic4.blank:
            pic7.locate(background, 306, 200)
            pic7.where = 4
            pic5.blank = True
            pic4.blank = False
        elif pic6.blank:
            pic7.locate(background, 706, 200)
            pic7.where = 6
            pic5.blank = True
            pic6.blank = False
        elif pic8.blank:
            pic7.locate(background, 506, 0)
            pic7.where = 8
            pic5.blank = True
            pic8.blank = False
    elif pic7.where == 6:
        if pic3.blank:
            pic7.locate(background, 706, 400)
            pic7.where = 3
            pic6.blank = True
            pic3.blank = False
        elif pic5.blank:
            pic7.locate(background, 506, 200)
            pic7.where = 5
            pic6.blank = True
            pic5.blank = False
        elif pic9.blank:
            pic7.locate(background, 706, 0)
            pic7.where = 9
            pic6.blank = True
            pic9.blank = False
    elif pic7.where == 7:
        if pic4.blank:
            pic7.locate(background, 306, 200)
            pic7.where = 4
            pic7.blank = True
            pic4.blank = False
        elif pic8.blank:
            pic7.locate(background, 506, 0)
            pic7.where = 8
            pic7.blank = True
            pic8.blank = False
    elif pic7.where == 8:
        if pic5.blank:
            pic7.locate(background, 506, 200)
            pic7.where = 5
            pic8.blank = True
            pic5.blank = False
        elif pic7.blank:
            pic7.locate(background, 306, 0)
            pic7.where = 7
            pic8.blank = True
            pic7.blank = False
        elif pic9.blank:
            pic7.locate(background, 706, 0)
            pic7.where = 9
            pic8.blank = True
            pic9.blank = False
    elif pic7.where == 9:
        if pic6.blank:
            pic7.locate(background, 706, 200)
            pic7.where = 6
            pic9.blank = True
            pic6.blank = False
        elif pic8.blank:
            pic7.locate(background, 506, 0)
            pic7.where = 8
            pic9.blank = True
            pic8.blank = False
        
    if pic1.where == 1 or pic1.where == 0:
        if pic2.where == 2 or pic2.where == 0:
            if pic3.where == 3 or pic3.where == 0:
                if pic4.where == 4 or pic4.where == 0:
                    if pic5.where == 5 or pic5.where == 0:
                        if pic6.where == 6 or pic6.where == 0:
                            if pic7.where == 7 or pic7.where == 0:
                                if pic8.where == 8 or pic8.where == 0:
                                    if pic9.where == 9 or pic9.where == 0:
                                        pic1.hide()
                                        pic2.hide()
                                        pic3.hide()
                                        pic4.hide()
                                        pic5.hide()
                                        pic6.hide()
                                        pic7.hide()
                                        pic8.hide()
                                        pic9.hide()
                                        re_start()
                                        start.show()

pic7.onMouseAction = pic7_onMouseAction

def pic8_onMouseAction(x, y, Action):
    if pic8.where == 1:
        if pic2.blank:
            pic8.locate(background, 506, 400)
            pic8.where = 2
            pic1.blank = True
            pic2.blank = False
        elif pic4.blank:
            pic8.locate(background, 306, 200)
            pic8.where = 4
            pic1.blank = True
            pic4.blank = False
    elif pic8.where == 2:
        if pic1.blank:
            pic8.locate(background, 306, 400)
            pic8.where = 1
            pic2.blank = True
            pic1.blank = False
        elif pic3.blank:
            pic8.locate(background, 706, 400)
            pic8.where = 3
            pic2.blank = True
            pic3.blank = False
        elif pic5.blank:
            pic8.locate(background, 506, 200)
            pic8.where = 5
            pic2.blank = True
            pic5.blank = False
    elif pic8.where == 3:
        if pic2.blank:
            pic8.locate(background, 506, 400)
            pic8.where = 2
            pic3.blank = True
            pic2.blank = False
        elif pic6.blank:
            pic8.locate(background, 706, 200)
            pic8.where = 6
            pic3.blank = True
            pic6.blank = False
    elif pic8.where == 4:
        if pic1.blank:
            pic8.locate(background, 306, 400)
            pic8.where = 1
            pic4.blank = True
            pic1.blank = False
        elif pic5.blank:
            pic8.locate(background, 506, 200)
            pic8.where = 5
            pic4.blank = True
            pic5.blank = False
        elif pic7.blank:
            pic8.locate(background, 306, 0)
            pic8.where = 7
            pic4.blank = True
            pic7.blank = False
    elif pic8.where == 5:
        if pic2.blank:
            pic8.locate(background, 506, 400)
            pic8.where = 2
            pic5.blank = True
            pic2.blank = False
        elif pic4.blank:
            pic8.locate(background, 306, 200)
            pic8.where = 4
            pic5.blank = True
            pic4.blank = False
        elif pic6.blank:
            pic8.locate(background, 706, 200)
            pic8.where = 6
            pic5.blank = True
            pic6.blank = False
        elif pic8.blank:
            pic8.locate(background, 506, 0)
            pic8.where = 8
            pic5.blank = True
            pic8.blank = False
    elif pic8.where == 6:
        if pic3.blank:
            pic8.locate(background, 706, 400)
            pic8.where = 3
            pic6.blank = True
            pic3.blank = False
        elif pic5.blank:
            pic8.locate(background, 506, 200)
            pic8.where = 5
            pic6.blank = True
            pic5.blank = False
        elif pic9.blank:
            pic8.locate(background, 706, 0)
            pic8.where = 9
            pic6.blank = True
            pic9.blank = False
    elif pic8.where == 7:
        if pic4.blank:
            pic8.locate(background, 306, 200)
            pic8.where = 4
            pic7.blank = True
            pic4.blank = False
        elif pic8.blank:
            pic8.locate(background, 506, 0)
            pic8.where = 8
            pic7.blank = True
            pic8.blank = False
    elif pic8.where == 8:
        if pic5.blank:
            pic8.locate(background, 506, 200)
            pic8.where = 5
            pic8.blank = True
            pic5.blank = False
        elif pic7.blank:
            pic8.locate(background, 306, 0)
            pic8.where = 7
            pic8.blank = True
            pic7.blank = False
        elif pic9.blank:
            pic8.locate(background, 706, 0)
            pic8.where = 9
            pic8.blank = True
            pic9.blank = False
    elif pic8.where == 9:
        if pic6.blank:
            pic8.locate(background, 706, 200)
            pic8.where = 6
            pic9.blank = True
            pic6.blank = False
        elif pic8.blank:
            pic8.locate(background, 506, 0)
            pic8.where = 8
            pic9.blank = True
            pic8.blank = False

    if pic1.where == 1 or pic1.where == 0:
        if pic2.where == 2 or pic2.where == 0:
            if pic3.where == 3 or pic3.where == 0:
                if pic4.where == 4 or pic4.where == 0:
                    if pic5.where == 5 or pic5.where == 0:
                        if pic6.where == 6 or pic6.where == 0:
                            if pic7.where == 7 or pic7.where == 0:
                                if pic8.where == 8 or pic8.where == 0:
                                    if pic9.where == 9 or pic9.where == 0:
                                        pic1.hide()
                                        pic2.hide()
                                        pic3.hide()
                                        pic4.hide()
                                        pic5.hide()
                                        pic6.hide()
                                        pic7.hide()
                                        pic8.hide()
                                        pic9.hide()
                                        re_start()
                                        start.show()
        

pic8.onMouseAction = pic8_onMouseAction

def pic9_onMouseAction(x, y, Action):
    if pic9.where == 1:
        if pic2.blank:
            pic9.locate(background, 506, 400)
            pic9.where = 2
            pic1.blank = True
            pic2.blank = False
        elif pic4.blank:
            pic9.locate(background, 306, 200)
            pic9.where = 4
            pic1.blank = True
            pic4.blank = False
    elif pic9.where == 2:
        if pic1.blank:
            pic9.locate(background, 306, 400)
            pic9.where = 1
            pic2.blank = True
            pic1.blank = False
        elif pic3.blank:
            pic9.locate(background, 706, 400)
            pic9.where = 3
            pic2.blank = True
            pic3.blank = False
        elif pic5.blank:
            pic9.locate(background, 506, 200)
            pic9.where = 5
            pic2.blank = True
            pic5.blank = False
    elif pic9.where == 3:
        if pic2.blank:
            pic9.locate(background, 506, 400)
            pic9.where = 2
            pic3.blank = True
            pic2.blank = False
        elif pic6.blank:
            pic9.locate(background, 706, 200)
            pic9.where = 6
            pic3.blank = True
            pic6.blank = False
    elif pic9.where == 4:
        if pic1.blank:
            pic9.locate(background, 306, 400)
            pic9.where = 1
            pic4.blank = True
            pic1.blank = False
        elif pic5.blank:
            pic9.locate(background, 506, 200)
            pic9.where = 5
            pic4.blank = True
            pic5.blank = False
        elif pic7.blank:
            pic9.locate(background, 306, 0)
            pic9.where = 7
            pic4.blank = True
            pic7.blank = False
    elif pic9.where == 5:
        if pic2.blank:
            pic9.locate(background, 506, 400)
            pic9.where = 2
            pic5.blank = True
            pic2.blank = False
        elif pic4.blank:
            pic9.locate(background, 306, 200)
            pic9.where = 4
            pic5.blank = True
            pic4.blank = False
        elif pic6.blank:
            pic9.locate(background, 706, 200)
            pic9.where = 6
            pic5.blank = True
            pic6.blank = False
        elif pic8.blank:
            pic9.locate(background, 506, 0)
            pic9.where = 8
            pic5.blank = True
            pic8.blank = False
    elif pic9.where == 6:
        if pic3.blank:
            pic9.locate(background, 706, 400)
            pic9.where = 3
            pic6.blank = True
            pic3.blank = False
        elif pic5.blank:
            pic9.locate(background, 506, 200)
            pic9.where = 5
            pic6.blank = True
            pic5.blank = False
        elif pic9.blank:
            pic9.locate(background, 706, 0)
            pic9.where = 9
            pic6.blank = True
            pic9.blank = False
    elif pic9.where == 7:
        if pic4.blank:
            pic9.locate(background, 306, 200)
            pic9.where = 4
            pic7.blank = True
            pic4.blank = False
        elif pic8.blank:
            pic9.locate(background, 506, 0)
            pic9.where = 8
            pic7.blank = True
            pic8.blank = False
    elif pic9.where == 8:
        if pic5.blank:
            pic9.locate(background, 506, 200)
            pic9.where = 5
            pic8.blank = True
            pic5.blank = False
        elif pic7.blank:
            pic9.locate(background, 306, 0)
            pic9.where = 7
            pic8.blank = True
            pic7.blank = False
        elif pic9.blank:
            pic9.locate(background, 706, 0)
            pic9.where = 9
            pic8.blank = True
            pic9.blank = False
    elif pic9.where == 9:
        if pic6.blank:
            pic9.locate(background, 706, 200)
            pic9.where = 6
            pic9.blank = True
            pic6.blank = False
        elif pic8.blank:
            pic9.locate(background, 506, 0)
            pic9.where = 8
            pic9.blank = True
            pic8.blank = False

    if pic1.where == 1 or pic1.where == 0:
        if pic2.where == 2 or pic2.where == 0:
            if pic3.where == 3 or pic3.where == 0:
                if pic4.where == 4 or pic4.where == 0:
                    if pic5.where == 5 or pic5.where == 0:
                        if pic6.where == 6 or pic6.where == 0:
                            if pic7.where == 7 or pic7.where == 0:
                                if pic8.where == 8 or pic8.where == 0:
                                    if pic9.where == 9 or pic9.where == 0:
                                        pic1.hide()
                                        pic2.hide()
                                        pic3.hide()
                                        pic4.hide()
                                        pic5.hide()
                                        pic6.hide()
                                        pic7.hide()
                                        pic8.hide()
                                        pic9.hide()
                                        re_start()
                                        start.show()

pic9.onMouseAction = pic9_onMouseAction

def end_onMouseAction(x, y, Action):
    endGame()

end.onMouseAction = end_onMouseAction

start.onMouseAction = start_onMouseAction



startGame(background)

