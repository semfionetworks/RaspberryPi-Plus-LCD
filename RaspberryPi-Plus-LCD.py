import lcdmodule as lcd
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
text = "* SemFio Sample * Python Script"
lcd.lcd_init()
if len(text) == 15:
    lcd.lcd_string(text,0,1)
else:
    lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
    lcd.lcd_string(text,0,1)
    lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
    lcd.lcd_string(text[16:],0,1)
