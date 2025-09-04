import SystemControl,Book,globcfg
import Input_box_lambda
import Button
from Gui import Gui

def main():
    Input_box_lambda
    print ("lamGen= %d" %globcfg.lamGen)     #lamGen affects the rate at which new threads or events are generated.
    print ("lamRW= %d" %globcfg.lamRW)       #lamRW affects the duration or execution time of individual threads.
    Button
    print ("Priority: %s" %globcfg.priority)
    book=Book.Book()
    g = Gui()
    generator=SystemControl.Generator(book, g)
    scheduler=SystemControl.Scheduler()


    generator.start()
    scheduler.start()

    # start Gui
    g.animation(50, 50, 5)

main()

