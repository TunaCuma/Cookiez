import time
from selenium import webdriver
from selenium.common.exceptions import *
import pygame

print("Press X on cookie bot window to save and close the game and program.")
print("The game will save itself every 100000 clicks.")

#####pygame#####
size = width,height = 300,300
vel = [2,2]
title = "Cookie bot"
window = pygame.display.set_mode(size)
pygame.display.set_caption(title)
pygame.init()
image = pygame.image.load('cookie.png')
window.blit(image,(0,0))
blue=(149,202,255)
white = (240,240,255)
font = pygame.font.SysFont(None,40)
mouse = pygame.Rect((0,0),(10,10))
window.blit(font.render("Tuna's cookie bot", True, blue), (25, 80))
button1 = pygame.draw.rect(window, blue, pygame.Rect((100, 150), (100, 30)))
window.blit(font.render('start', True, white), (110, 150))
button2 = pygame.draw.rect(window, blue, pygame.Rect((100, 200), (100, 30)))
window.blit(font.render('stop', True, white), (110, 200))
rectpos = (0,0)
########bringsave#########

with open("cookiesave.txt","r",encoding="utf-8") as file:
    save = file.read()
browser = webdriver.Chrome()
url = "https://orteil.dashnet.org/cookieclicker/"
browser.get(url)
time.sleep(7) #change for your internet speed
cookie = browser.find_elements_by_xpath('//*[@id="bigCookie"]')
cookie = cookie[0]

##########functions#############
def opensavegame():
    browser.find_element_by_xpath('//*[@id="prefsButton"]').click()
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="menu"]/div[3]/div[3]/a[2]').click()
    browser.find_element_by_xpath('//*[@id="textareaPrompt"]').send_keys(save)
    browser.find_element_by_xpath('// *[ @ id = "promptOption0"]').click()
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="menu"]/div[1]').click()
def savegame():
    browser.find_element_by_xpath('//*[@id="prefsButton"]').click()
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="menu"]/div[3]/div[3]/a[1]').click()
    time.sleep(1)
    save = browser.find_element_by_xpath('//*[@id="textareaPrompt"]').text
    time.sleep(1)
    with open("cookiesave.txt", "w", encoding="utf-8") as file:
        file.write(save)
    browser.find_element_by_xpath('//*[@id="promptOption0"]').click()
    browser.find_element_by_xpath('//*[@id="menu"]/div[1]').click()
    global click
    print("clicked {} times and saved sucessfully".format(click))
def close():
    savegame()
    pygame.quit()
    browser.close()
    run = False
#######################starting#############################

golden= 0
click = 0
status = "d" #d means stop b means start
opensavegame()
run = True



while run:
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            rectpos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse.colliderect(button1):
                status = "b"
            if mouse.colliderect(button2):
                status = "d"
        if event.type == pygame.QUIT:
            close()
    mouse = pygame.Rect((rectpos), (1, 1))
    keys = pygame.key.get_pressed()
    product , upgrade = None , None
    if click % 100000 == 0 and click != 0:
        savegame()
    if keys[pygame.K_b]:
        status = "b"
    if keys[pygame.K_d]:
        status = "d"
    if status == "b":
        try:
            cookie.click()
            click+=1
        except  ElementClickInterceptedException:
            pass
        except StaleElementReferenceException:
            pass
        if not upgrade:
            try:
                upgrade = browser.find_elements_by_class_name('crate.upgrade.enabled')
                if upgrade:
                    upgrade[-1].click()
            except NoSuchElementException:
                pass
            except  ElementClickInterceptedException:
                pass
            except StaleElementReferenceException:
                pass
        if not product:
            try:
                product = browser.find_element_by_class_name('product.unlocked.enabled')
                product.click()
            except NoSuchElementException:
                pass
            except  ElementClickInterceptedException:
                pass
            except StaleElementReferenceException:
                pass
        try:
            goldenCookie = browser.find_element_by_class_name("shimmer")
            goldenCookie.click()
            golden+=1
            print(golden ,". golden cookie has been clicked")
        except NoSuchElementException:
            pass
        except  ElementClickInterceptedException:
            pass
        except  ElementNotInteractableException:
            pass
        except StaleElementReferenceException:
            pass
    #to break program press escape or X in cookie bot window

    if keys[pygame.K_ESCAPE]:
        close()