from p5 import *

def setup():  
  global input 
  global fade
  global button
  global content  
  global stationNumber
  stationNumber = 1
  fade = 0
  coordinateMode(LEFT_HAND)
  createCanvas(displayWidth, 3000);
  background("black")
  fill("white") 
  

  # extension idea: change the font size and family
  textSize(18)
  textFont('monospace')
  content = "🧍🏼 You are standing on a road heading from South to North. 🚧 There is a sign alongside the road. What do you want to do?"

  input = createInput()
  #extension: style the input and text
  input.position(0, 0, 'fixed')
  input.size(300)
  button = createButton("submit")
  button.position(300, 0, 'fixed')
  
def draw():
  global fade
  global button
  global content

  if stationNumber == 1:
    button.mousePressed(station1)
  elif stationNumber == 2:
    button.mousePressed(station2)
  elif stationNumber == 3:
    button.mousePressed(station3)
  elif stationNumber == 4:
    button.mousePressed(station4)
  elif stationNumber == 5:
    button.mousePressed(station5)
  elif stationNumber == 6:
    button.mousePressed(station6)
  
  fadeAmount = 0.05
  fill(0, 200, 0, fade)

  text(content, 0, 50, 800)
 
  if fade < 255:
    fade += fadeAmount
 

def station1():
  global input
  global content
  global stationNumber
  
  if input.value() == "read the sign": 
    content = content + """\n\n      -------------------------------------
    | WELCOME TO THE EMPIRE OF MATHLAND |    
    -------------------------------------
    """
    
# question: what is """ used for in Python?

  elif input.value() == "go North": 
    content = content + "\n\n Before long you get to a Castle 🏰. The gate is closed and there is a builder standing besides it. What do you want to do?"
    stationNumber = 2

  elif input.value() == "go South":
    content = content + "\n\n The way is blocked by an invisible wall."

  else:
    content = content + "\n\n Sorry, you can't do that."


def station2():
  global input
  global content
  global stationNumber
  
  # subject: Pythagorean Theorem
  if input.value() == "talk to builder":
    content = content + "\n\n 🤷‍♂️'Hi there!' he says. 'Sorry I can't help you now, I need to fix this gate and I've forgotten the Pythagorean Theorem! I'm in so much trouble...'"

  elif input.value() == "tell Pythagorean Theorem":
    content = content + "\n\n 'Oh my!', he exclaims excitedly. 'You know it? Please tell me'."

  elif input.value() == "open gate":
    content = content + "\n\n The gate seems stuck. Maybe because the builder is working on it."


# extension question: escape characters
# extension question: what is ASCII, what is UNICODE. How many bits in either?
  elif input.value() == "look at gate":
    content = content + """ 
........................................................................
..................................{}.{}.................................
..........................!..!..!.II.II.!..!..!.........................
.......................!..I__I__I_II II_I__I__I..!......................
.......................I_/|__|__|_|| ||_|__|__|\_I......................
....................!./|_/|  |  | || || |  |  |\_|\ !...................       
.........--.........I//|  |  |  | || || |  |  |  |\\\I.........--........
......./-   \....! /|/ |  |  |  | || || |  |  |  | \|\!...../=   \\......
.......\=__ /....I//|  |  |  |  | || || |  |  |  |  |\\\I....\-__ /......
........}  {..! /|/ |  |  |  |  | || || |  |  |  |  | \|\!...}  {.......
.......{____} I//|  |  |  |  |  | || || |  |  |  |  |  |\\\I.{____}......
._!__!__|= |=/|/ |  |  |  |  |  | || || |  |  |  |  |  | \|\=|  |__!__!_
._I__I__|  ||/|__|__|__|__|__|__|_|| ||_|__|__|__|__|__|__|\||- |__I__I_
.-|--|--|- ||-|--|--|--|--|--|--|-|| ||-|--|--|--|--|--|--|-||= |--|--|-
. |  |  |  || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||  |  |  |
. |  |  |= || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||= |  |  |
. |  |  |- || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||= |  |  |
. |  |  |- || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||- |  |  | 
._|__|__|  ||_|__|__|__|__|__|__|_|| ||_|__|__|__|__|__|__|_||  |__|__|_
.-|--|--|= ||-|--|--|--|--|--|--|-|| ||-|--|--|--|--|--|--|-||- |--|--|-
.-|--|--|| |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||= |  |--|--|-
.~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~
    """ 


  elif input.value() == "a squared plus b squared equals c squared":
    content = content + "\n\n 🕺'That's it', exclaims the builder. There is a flurry of activity and soon the gate is opened.\n    The road stretches ahead in a straight line. You see an old man by the gate, looking puzzedly at a map."
    stationNumber = 3
  

def station3():    
  global input 
  global content
  global stationNumber
  global featheredCap

  # learning objective: apply the Pythagorean Theorem to triangles
  if input.value() == "talk to old man":
    content = content + "\n\n 👴🗺️The old man says: 'I just can't work it out. What is the distance in kilometers from here to Horse Town? I can only see that this town has coordinates (x: 100, y: 50) and Horse Town's are (x: 150, y: 20)."

  elif input.value() == "look at old man":
    content = content + """

................,.............
.............,:' `..;.........
.............`. ,;;'%.........
.............+;;'%%%%%........
............../- %,)%%........
..............`   \ %%........
...............=  )/ \\........
...............`-'/ / \\.......
................./\/.-.\\......
................|  (    |.....
................|  |   ||.....
................|  |   ||.....
............_.-----'   ||.....
.........../ \________,'|.....
..........(((/..|       |.....
..........//....|       |.....
.........//.....|\      |.....
........//......| \     |.....
.......//.......|  \    |.....
......//........|   \   |.....
.....//.........|    \  |.....
....//..........|    |\ |.....
...//...........|    | \|.....
..//............\    \\........
.c'.............|\    \\.......
................| \    \\......
................|  \    \\.....
................|.' \    \\....
..............._\    \.-' \\...
...............(___.-(__.'\/..
    """


  elif input.value() == "40":
    content = content + "\n\n 'Ahh, that's it! Please accept this small gift as a token of appreciation.' You receive the feathered cap 👒.\n The old man walks off. A posh looking lady is strolling down the street in your direction 👸."
    featheredCap = 1
    stationNumber = 4

  elif input.value() == "¯\(°_o)/¯":
    content = content + "\n\n Yeah, me neither."


def station4():
  global input 
  global content
  global stationNumber
  global featheredCap
  global wearingFeatheredCap  

  # subject: Pythagorean Theorem and Vectors
  # learning objective: Negatives in coordinate geometry
  if input.value() == "wear feathered cap":
    if featheredCap == 1:
      content = content + "\n\n You look great!"
      wearingFeatheredCap = 1
    else:
      content = content + "\n\n You don't have that."


  elif input.value() == "look at feathered cap":
    if featheredCap == 1:
      content = content + """
      .................
      ............(/;..
      ...........(/;...
      .....--..-(/;....
      ....|    (/;.....
      ..__|====/='__...
      .(____________)..
      .................
      """

    else:
      content = content + "\n\n You don't have that."


  elif input.value() == "look at posh lady":
    content = content + """
     ...................
     .......//`\\........
     ......(/a a\)......
     ......(\_-_/)......
     ......-~'='~-......
     ..../`~`"Y"`~`\\....
     .../ /(_ * _)\ \\...
     ../ /  )   (  \ \\..
     ..\ \_/\\\_//\_/ /..
     ...\/_) '*' (_\/...
     .....|       |.....
     .....|       |.....
     .....|       |.....
     .....|       |.....
     .....|       |.....
     .....|       |.....
     .....|       |.....
     .....w*W*W*W*w.....
     ...................
     """

  elif input.value() == "talk to posh looking lady":
    if wearingFeatheredCap == 0:
      content = content + "\n\n The lady ignores you."
    
    elif wearingFeatheredCap == 1:    
      content = content + """\n\n The lady greets you. She says: 'Maybe you can help me, Ivé lost my mechanical owl.

      /(°^°)\\

      He was programmed to fly in 3 different vectors, first (x: 10, y: 5), then (x: -20, y: 25) and lastly (x: -20, y: 10). All in meters. Where do you think he might be now 🗺️?'"""
      stationNumber = 5
      
  
def station5():
  global input    
  global content
  global stationNumber

  # learning objective: Apply the Pythagorean Theorem to distances
  if input.value() == "(x: -30, y: 40)":
    content = content + "\n\n 'That sounds about right. How many meters away do you think that might be 📏?'"
    stationNumber = 6
    
  else:
    content = content + "\n\n 'Hmmm, that doesn't sound right."


def station6():
  global input    
  global content
  global stationNumber

  # learning objective: Solve problems involving angles
  if input.value() == "50":
      content = content + "\n\n 'That sounds about right. So, which angle would I need to walk in to get there 🧭?'"
    


  






