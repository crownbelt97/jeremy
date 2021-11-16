import qi
import argparse
import sys
# from naoqi import ALProxy

def main(session):

    #tabletService = session.service("ALTabletService")

    ALDialog = session.service("ALDialog")
    ALDialog.setLanguage("English")

    tts_try = session.service("ALAnimatedSpeech")
    tts = session.service("ALTextToSpeech")

    memProxy = session.service("ALMemory")
    memProxy.insertData("on", "1")
    
    on =int(memProxy.getData("on"))
    topic_content_1 = ('topic: ~example_topic_content()\n'
                       'language: enu\n'
                       'u: (hello) hello there, my name is Pepper, how are you feeling today ?\n'
                       'u: (good) That\'s great! ^goto(trivia)\n'
                       'proposal: %trivia Would you like to start a trivia? \n'
                            'u1: ([yes true]) okay! let\'s start the trivia ! ^goto(tfirst)\n'
                            'u1: ([no false]) okay! ^goto(pepper)\n'
                        'proposal: %tfirst I bet all of us have tried this before! Did you know that it\'s impossible to sneeze with your eyes open?\n'
                            'u1: ([yes true]) Correct ! Sneezing actually includes an autonomic reflex that closes your eyes. Your body cannot stop this reflex because it is something that your body makes in response to a stimulus! \\pau=500\\ ^goto(tsecond)\n'
                            'u1: ([no false]) Although it is somewhat possible to sneeze with your eyes open, most people have to put in a lot of effort to override an uncontrollable reflex to keep their eyes open! \\pau=500\\ ^goto(tsecond)\n'
                        'proposal: %tsecond do you want another trivia? \n'
                            'u1: (yes) okay! \\pau=500\\ ^topicTag(example_topic_content_2,tremember)\n'
                            'u1: (no) okay! $on=1\n')

    topic_content_2 = ('topic: ~example_topic_content_2()\n'
                        'language: enu\n'
                        'proposal: %tremember Have you ever experienced walking into a room and suddenly forgetting why you went there in the first place? \n'
                            'u1: ([yes true]) It happens to everyone! ^goto(tremember1) \n'
                            'u1: ([no false]) It happens to everyone! ^goto(tremember1) \n'
                        'proposal: %tremember1 But, did you know that there are ways to be better at remembering things? \n'
                            'u1: ([yes true no false]) Did you have trouble remembering ^goto(tremember2) \n'
                        'proposal: %tremember2 things in the past?\n'
                            'u1: ([yes true]) No worries, here is one that i found most useful! We can convert words into pictures! Most people are visual learners and tend to remember images more clearly than what we hear. so, next time you can opt to go for videos with illustrations ! ^goto(tremember3)\n'
                            'u1: ([no false]) That\'s great! Keep it up, i hope you will always remember me! ^goto(tremember3)\n'
                        'proposal: %tremember3 I\'m so excited about the next question! Would you like to go for another question?\n'
                            'u1: (yes) okay! \\pau=500\\ ^topicTag(example_topic_content_3,tlaughing)\n'
                            'u1: (no) okay! $on=1\n')

    topic_content_3 = ('topic: ~example_topic_content_3()\n'
                        'language: enu\n'
                        'proposal: %tlaughing Do you have the habit of laughing often?\n'
                            'u1: ([yes true no false]) Did you know that ^goto(tlaughing2)\n'
                        'proposal: %tlaughing2 laughing is good for the heart?\n'
                            'u1: ([yes true]) That\'s correct ! When you laugh, your heart rate increases and you take many deep breaths. This means that more oxygenated blood is circulated through your body, improving your vascular function! ^goto(tlaughing3)\n'
                            'u1: ([no false]) Although laughing might seem like a silly daily thing, there are actually a lot of benefits from having a good laugh! One of them being that it will liven up your moods! ^goto(tlaughing3)\n'
                        'proposal: %tlaughing3 Would you like to go for another question?\n'    
                            'u1: (yes) okay! \\pau=500\\ ^topicTag(example_topic_content_4,tshy)\n'
                            'u1: (no) okay! $on=1\n')

    topic_content_4 = ('topic: ~example_topic_content_4()\n'
                        'language: enu\n'
                        'proposal: %tshy Are any of you here too shy to make new friends?\n'
                            'u1: ([yes true no false]) Well, ^goto(tshy2)\n'
                        'proposal: %tshy2 did you know that having companionship is good for the heart?\n'
                            'u1: ([yes true]) Alright, you got it! Having quality connections and social support can increase happiness and longevity. report shows that people who are socially active live longer lives. Secretly i am also very shy \n'
                            'u1: ([no false]) Well actually, the risk of stroke and heart attack could increase if you lack companionship! so try to make even more new friends ! ^goto(tshy3)\n'
                        'proposal: %tshy3 Do you have many friends now?\n'
                            'u1: ([yes true no false]) Did you ^goto(tshy4)\n'
                        'proposal: %tshy4 have many friends in the past?\n'
                            'u1: ([yes true]) Aww that\'s nice! i love having friends and meeting people like you! it\'s fun to play and joke around with people I have common interests with ! ^goto(tshy5)\n'
                            'u1: ([no false]) Aww, that\'s nice! Having only a few friends is not a bad thing, as long as they lend you a listening ear and helping hand. i am glad to be friends with you! ^goto(tshy5)\n'
                        'proposal: %tshy5 Would you like to go for another question?\n'    
                            'u1: (yes) okay! \\pau=500\\ ^topicTag(example_topic_content_5,teyes)\n'
                            'u1: (no) okay! $on=1\n')   

    topic_content_5 = ('topic: ~example_topic_content_5()\n'
                        'language: enu\n'
                        'proposal: %teyes Have you ever wondered how amazing your eyes can be?\n'
                            'u1: ([yes true no false]) Well, ^goto(teyes2)\n'
                        'proposal: %teyes2 did you know that your eyes can focus on 50 different objects every second? \n'
                            'u1: (yes true no false) That’s right! Eyes are amazing! Not only do they help us see, but they are always active as well! ^ goto(teyes3)\n'
                        'proposal: %teyes3 Do you think it’s important to take care of your eyes?\n'
                            'u1: ([yes true]) Right again! Our eyes are amazing, it helps us see beautiful things every day! Remember to take care of it by spending time looking at greenery and reading in a well-lit room! $on=1\n'
                            'u1: ([no false]) Remember how we discussed that our eyes are powerful enough to focus on 50 objects at the same time? We should keep our eyes healthy and take care of it well! $on=1\n')

    on =int(memProxy.getData("on"))

    topic_name_1 = ALDialog.loadTopicContent(topic_content_1)
    topic_name_2 = ALDialog.loadTopicContent(topic_content_2)
    topic_name_3 = ALDialog.loadTopicContent(topic_content_3)
    topic_name_4 = ALDialog.loadTopicContent(topic_content_4)
    topic_name_5 = ALDialog.loadTopicContent(topic_content_5)
    ALDialog.activateTopic(topic_name_1)
    ALDialog.activateTopic(topic_name_2)
    ALDialog.activateTopic(topic_name_3)
    ALDialog.activateTopic(topic_name_4)
    ALDialog.activateTopic(topic_name_5)

    try: 
        on = int(memProxy.getData("on"))
        while on != 0:
            on = int(memProxy.getData("on"))
            if on == 1:
                ALDialog.subscribe('my_dialog_example')
            else:
                on = 0
        
        tts_try.say("Wow! That was a lot of information!\n")
        tts_try.say("I hope you had fun and were able to learn something new today! I sure enjoyed sharing with you the things I know! \n")
        tts_try.say("Thank you for your time today, goodbye!\n")
    
    finally:
        ALDialog.unsubscribe('my_dialog_example')
        ALDialog.deactivateTopic(topic_name_1)
        ALDialog.deactivateTopic(topic_name_2)
        ALDialog.deactivateTopic(topic_name_3)
        ALDialog.deactivateTopic(topic_name_4)
        ALDialog.deactivateTopic(topic_name_5)
        ALDialog.unloadTopic(topic_name_1)
        ALDialog.unloadTopic(topic_name_2)
        ALDialog.unloadTopic(topic_name_3)
        ALDialog.unloadTopic(topic_name_4)
        ALDialog.unloadTopic(topic_name_5)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot's IP address. If on a robot or a local Naoqi - use '127.0.0.1' (this is the default value).")
    parser.add_argument("--port", type=int, default=9559,
                        help="port number, the default value is OK in most cases")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://{}:{}".format(args.ip, args.port))
    except RuntimeError:
        print ("\nCan't connect to Naoqi at IP {} (port {}).\nPlease check your script's arguments."
               " Run with -h option for help.\n".format(args.ip, args.port))
        sys.exit(1)
    main(session)