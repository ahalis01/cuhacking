# twitter written by Connor Ciavarella

# import modules
import twitter
import creds
import string

# checks if bot is in check. if 1 then bot is in, if 0 then bot isnt
def instring(check):
    for i in range(len(check)):
        character = check[i].lower()
        if character == 'b':
            if i != 0:
                if (ord(check[i - 1].lower()) < 97 or ord(check[i - 1].lower()) > 122):
                    if (ord(check[i + 3].lower()) < 97 or ord(check[i + 3].lower()) > 122):
                        if check[i + 1].lower() == 'o' or check[i + 1].lower() == '0':
                            if check[i + 2].lower() == 't' or check[i + 1].lower() == '+':
                                return 1

            else:
                if (ord(check[i + 3].lower()) < 97 or ord(check[i + 3].lower()) > 122):
                    if check[i + 1].lower() == 'o' or check[i + 1].lower() == '0':
                        if check[i + 2].lower() == 't' or check[i + 1].lower() == '+':
                            return 1

    return 0
                        
        

# grabs the user whos name is provided information
def usertweet(name):
    data = []
    
    #Twitter API credentials
    consumer_key = creds.creds[0]
    consumer_secret = creds.creds[1]
    access_key = creds.creds[2]
    access_secret = creds.creds[3]

    api = twitter.Api(consumer_key= consumer_key,
                  consumer_secret= consumer_secret,
                  access_token_key= access_key,
                  access_token_secret= access_secret)

    # grab the users data
    try:
        results = api.GetUser(screen_name = name, return_json = True)

    # if user doesnt exist return empty list
    except twitter.error.TwitterError:
        return []

    for attribute in results:
        attribute.encode('unicode-escape').decode('utf-8')

    #gets rid of emojis in name or description
    printable = set(string.printable)

    results["screen_name"] = ''.join(filter(lambda x: x in printable, results["screen_name"]))
    results["description"] = ''.join(filter(lambda x: x in printable, results["description"]))

    # list of relevent data parameters
    data = [results["screen_name"],
            results["description"],
            results["name"],
            results["followers_count"],
            results["friends_count"],
            results["listed_count"],
            results["favourites_count"],
            results["verified"],
            results["statuses_count"],
            results["created_at"],
            results["id"]
            ]

    # checks if bot is in name
    namedesc = instring(results["screen_name"])

    # if bot isnt in name then check the description
    if namedesc == 0:
        namedesc = instring(results["description"])

    # if namedesc == 1 then user has bot in their description or name
    data.append(namedesc)

    # return the data
    return data


        

    
    
    

