# Readme for adventure game

# 21 projects - 9 hours of pytho projects

Youtube tutorial link:

```bash
https://youtu.be/NpmFbWO6HPU?si=ZWpvWuc8HL24-uHX
```

simulate progress bar:
# Function to simulate progress bar
```python
def progress_bar():
    for _ in range(10):
        print(Fore.YELLOW + "█", end="", flush=True)
        time.sleep(0.5)
    print(Style.RESET_ALL)
```

### storyline
ill let you know  the whole storyline and briefing then you will impliment that, first understand the storyline: Story: Escaping the forest and The Tale of Fadedhood first understand that i m making this game as 5 levels, but for simplicity first we will be making the level 1 only, and later we can clone and change the inputs etc, and levels in sense that when it is started, on top will be small brief that we have to escape the forest and find the fadedhood town for settling, and then we will mention that there are 5 levels and we need to pass thru each puzzle type adventure and go thru all. like we will print that Level 1 and then the input start of the scene that we are no where but between the very high trees forest, with ways left right  and ahead is a border with door. so we will get input from player that which option they would like to select, thenaccording to that options make the game interactive like the door should be tried to open but it will be locked, then player will try to choose remainaing other options which were to go right or left, and on left will be different adventure  with something new and on right will be different adventure with somthing new, this is like apuzzle game where we go and explore options and see how to escape the forest. each input should be asked from user about what they want to do with and according to that game should continue, after 3 or 4 prompts user will get msg that they passed level 1 and now level 2 started. for level 2 we will write code later by cloning the first level and will change the options and obstacles etc but rihgt now just make this and impliment this for level one so i can see if it works fine. if you dont under stand or want to clarify any confusion please ask so i can confirm. the story brief is below jsut for reference:

Level 1: The Journey Begins

    The player sets out on a journey from their hometown of Fadedhood, a quaint village nestled at the edge of the Enchanted Forest.
    They encounter Faded, a mysterious traveler with a shadowy past, who joins them on their quest for adventure.
    Together, they venture into the heart of the forest in search of the elusive Crystal of Wisdom.

Level 2: The Forest Guardians

    The player and Faded encounter the Forest Guardians, ancient spirits who protect the secrets of the Enchanted Forest.
    They must prove their worthiness through tests of courage, wisdom, and compassion to earn the guardians' trust.
    Faded's hidden talents and past deeds come to light, revealing a deeper connection to the forest and its guardians.

Level 3: The Hidden Path

    The player and Faded uncover a hidden path leading to the heart of the forest, where the Crystal of Wisdom awaits.
    They must navigate treacherous terrain and overcome perilous obstacles to reach their destination.
    Faded's true identity and purpose are revealed, shaping the outcome of their quest for the Crystal. i like the variation two of tale of fadedhood, but i want some changes, like first i decided to make the game upto 5 levels only and not 10 to make it interesting and concise, the Faded should be a very twist character like user wont be knowing the outcome etc, but dont make the Faded as a top superior type person, make him a down to earth but some mysterious person who should remain mysterious till end and user wont know much about him , the game scenes need to be shifted to a better story like thru a forest and finding some mysterious place or town abondoned which is Fadedhood, like the main storyline should be that we have to escape the forest and find the fadedhood town for shelter, and finding the fadedhood town should be in the last level 5 before that we need to escape the forest and reach there also dont make it sound like a magical or something, make it real and engaging, dont add magical spell type things and make the aim of game something better, like the purpose of game which user will know and will try to reach till level 5 by going thru all the storyline, make it trilling, with twists and all fun stuff, now make this in python with all the requirements of colors, ,the grayed colored texts which represents the deep talks or etc and all the things reaching till the level 5 , with the progress bar system that i already explained. now i want the perfect code with no mistakes, you can add as many if else and elif statements that you like but the storyline should continue and user should be engaged till end and user will on every option decide what to do etc

    
## Ai voice characters
sean normal tone character for playing character sound
killian the vampire high tone character for the faded player and game options too



## AScii art

### home
```bash
       ^  ^  ^   ^      ___I_      ^  ^   ^  ^  ^   ^  ^
      /|\/|\/|\ /|\    /\-_--\    /|\/|\ /|\/|\/|\ /|\/|\
      /|\/|\/|\ /|\   /  \_-__\   /|\/|\ /|\/|\/|\ /|\/|\
      /|\/|\/|\ /|\   |[]| [] |   /|\/|\ /|\/|\/|\ /|\/|\
```

               ,@@@@@@@,
       ,,,.   ,@@@@@@/@@,  .oo8888o.
    ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o
   ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'
   %&&%&%&/%&&%@@\@@/ /@@@88888\88888'
   %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'
   `&%\ ` /%&'    |.|        \ '|8'
       |o|        | |         | |
       |.|        | |         | |
    \\/ ._\//_/__/  ,\_//__\\/.  \_//__/_



              v .   ._, |_  .,
           `-._\/  .  \ /    |/_
               \\  _\, y | \//
         _\_.___\\, \\/ -.\||
           `7-,--.`._||  / / ,
           /'     `-. `./ / |/_.'
                     |    |//
                     |_    /
                     |-   |
                     |   =|
                     |    |
--------------------/ ,  . \--------._



                  _.._
   _________....-~    ~-.______
~~~                            ~~~~-----...___________..--------
                                           |   |     |
                                           | |   |  ||
                                           |  |  |   |
                                           |'. .' .`.|
___________________________________________|0oOO0oO0o|____________
 -          -         -       -      -    / '  '. ` ` \    -    -
      --                  --       --   /    '  . `   ` \    --
---            ---          ---       /  '                \ ---
     ----               ----        /       ' ' .    ` `    \  ----
-----         -----         ----- /   '   '        `      `   \
      -----          ------     /          '    . `     `    `  \
            -------           /  '    '      '      `
                    --------/     '     '   '



                   \   |   /            _\/_
                     .-'-.              //o\  _\/_
  _  ___  __  _ --_ /     \ _--_ __  __ _ | __/o\\ _
=-=-_=-=-_=-=_=-_= -=======- = =-=_=-=_,-'|"'""-|-,_ 
 =- _=-=-_=- _=-= _--=====- _=-=_-_,-"          |
jgs=- =- =-= =- = -  -===- -= - ."


                 .,
        .    ____/__,
      .' \  / \==\```
     /    \ 77 \ |
    /_.----\\__,-----.
<--(\_|_____<__|_____/
    \  ````/|   ``/```
     `.   / |    I|
       `./  |____I|
            !!!!!!!
            | | I |
            | | I |
            \ \ I |
            | | I |
           _|_|_I_|
          /__/____| 



      _,.
    ,` -.)
   ( _/-\\-._
  /,|`--._,-^|            ,
  \_| |`-._/||          ,'|
    |  `-, / |         /  /
    |     || |        /  /
     `r-._||/   __   /  /
 __,-<_     )`-/  `./  /
'  \   `---'   \   /  /
    |           |./  /
    /           //  /
\_/' \         |/  /
 |    |   _,^-'/  /
 |    , ``  (\/  /_
  \,.->._    \X-=/^
  (  /   `-._//^`
   `Y-.____(__}
    |     {__)
          ()



  ,   A           {}
 / \, | ,        .--.
|    =|= >      /.--.\
 \ /` | `       |====|
  `   |         |`::`|
      |     .-;`\..../`;_.-^-._
     /\\/  /  |...::..|`   :   `|
     |:'\ |   /'''::''|   .:.   |
      \ /\;-,/\   ::  |..:::::..|
      |\ <` >  >._::_.| ':::::' |
      | `""`  /   ^^  |   ':'   |
      |       |       \    :    /
      |       |        \   :   /
      |       |___/\___|`-.:.-`
      |        \_ || _/    `
      |        <_ >< _>
      |        |  ||  |
      |        |  ||  |
      |       _\.:||:./_
      | jgs  /____/\____\




                               _
                           ,--.\`-. __
                         _,.`. \:/,"  `-._
                     ,-*" _,.-;-*`-.+"*._ )
                    ( ,."* ,-" / `.  \.  `.
                   ,"   ,;"  ,"\../\  \:   \
                  (   ,"/   / \.,' :   ))  /
                   \  |/   / \.,'  /  // ,'
                    \_)\ ,' \.,'  (  / )/
                        `  \._,'   `"
                           \../
                           \../
                 ~        ~\../           ~~
          ~~          ~~   \../   ~~   ~      ~~
     ~~    ~   ~~  __...---\../-...__ ~~~     ~~
       ~~~~  ~_,--'        \../      `--.__ ~~    ~~
   ~~~  __,--'              `"             `--.__   ~~~
~~  ,--'                                         `--.
   '------......______             ______......------` ~~
 ~~~   ~    ~~      ~ `````---"""""  ~~   ~     ~~
        ~~~~    ~~  ~~~~       ~~~~~~  ~ ~~   ~~ ~~~  ~
     ~~   ~   ~~~     ~~~ ~         ~~       ~~   SSt
              ~        ~~       ~~~       ~

------------------------------------------------
Thank you for visiting https://asciiart.website/
This ASCII pic can be found at
https://asciiart.website/index.php?art=nature/islands




                                  
      .              .   .'.    
    \   /      .'. .' '.'   ' 
  -=  o  =-  .'   '              
    / | \                        
      |                           
      |                         
      |                      
      |=====.               
      ||=o=||              
      ||   ||                
      ||   ||              
      ||___||               
      |[:::]|                
      '-----'



                                                                                                                                                                            
                                   ░░░░                                                                                                                                     
        ▒▒▒▒▒▒▒                  ░░░░░░░░                                                                                                                                   
     ▒▒▒▒▒▒▒▒▒▒▒▒▒              ░░░░░░░░░░                                                             
   ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒             ░░░░▓░░░░░                             
   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒          ░░░░░░▓░░░░░░                        
  ▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒         ░░░░░░░▓░░░░░░░                          
  ▒▒▒▒▒▒▒▓▒▓▒▒▒▒▒▒▒▒        ░░░░░▒▓░▓░░░░░░░                        
   ▒▒▒▒▒▒▒▓▓▒▓▓▓▓▒▒▒         ░░░░░░▓▓░░░░░░░                     
   ░▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒           ░░░░░░▓░▓░░░░                    
     ░▒▒▓▓▓▓▒▒▒▒▒             ░░░░░░▓▓░░░░░░                      
         ▓▓▓                 ░░░▓░░░▓░░░░░░░░                
          ▓▓                ░░░░░▓░░▓░░░░░░░░░           
          ▓▓               ░░░░░░░░▓▓░░░░▓░░░░░          
          ▓▓               ░░░░░░░░░▓░░▒▓░░░░░░            
          ▓▓               ░░░░░░░░░▓▓▓░░░░░░░░           
         ▒▓▓                 ░░░░░░▒▓▒░░░░░░░                 
         ▓▓▓                       ▒▓▓                          
         ▓▓▓                       ▓▓▓                      
         ▓▓▓                       ▓▓▓              
                                                                                                                                                                   
                                        