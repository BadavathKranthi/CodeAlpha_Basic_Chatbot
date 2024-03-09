import re
import long_responses as long
def message_probability(user_messsages, recognised_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_word = True
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1
    # claculates the percent of recognised words in a user message
    percentage = float(meaasge_certainty)/float(len(recognised_words))
    # check that the required words are in the string
    for word in required_words:
       if word not in user_message:
          has_required_word = False
          break
    if has_required_word or single_response:
       return int(percentage*100)
    else:
       return 0

def check_all_messages(message):
    highest_prob_list = {}
    def response(bot_response, list_of_words, single_response=False, required_words=-[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = bmessage_probability(message, list, single_response, required_words)
    #Response--------------------------------------------------------------
    response('Hello!',['hellow', 'hi', 'sup', 'hey', 'heyo'], single_response=True)
    response('I\'m doing fine, and you?', ['how','are', 'you', 'doing'],required_words=['how'])
    response('Thank you!',['i','love','code','palace'], required_words=['code', 'palace'])
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    print(highest_prob_list)
    return best_match
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_message(split_message)
    return response
# Testing the response system
while True:
    print('Bot: ' + get_response(input('you: ')))
