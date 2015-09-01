import sys,os
import requests

# r = requests.get('https://graph.facebook.com/v2.4/275476105939521/feed?access_token=CAACEdEose0cBAAZC4THXFZBThHxWgcOpzFk1tPdi3Jac2hCGYUEuVvfvud1FisZCw1cuZBZCKBhtAZCeFl1efkhXUMcDvoBONhi8NnLseDojoYhDQYQA5W2OqMl5dRPLBilpijD6brsItL0BsQqF2MCTjOeZBnZA9EwZBRd4MN7xvhfGG0D0M3gF1KZBhpzvp74SNRm60dBqbIE5z8K5jHJaCV')
#
# print r.text
def post_on_page(message):
    request = 'curl -i -X POST \-d "'+message+'" -d "access_token=CAACEdEose0cBAJwg4MK4qGFTk810BaMK4Al1d6oIf1AER4U9bKjm9S4ahkZCkjeJVDRjKLq0LavrRZCApMaDnejOz7hEjvDmtZCQxvZBR3fZBx0GvQzpbXLx8yucs6YTOgeXBIPo2aMON7xUSboBZAv8SKH9G9G84HJW59dryMdDbR39ltJaxQZBIln4YR6CAA1C6dNzNKl3gZDZD"\"https://graph.facebook.com/v2.4/275476105939521/feed"'
    r = os.system(request)
    return r


message = raw_input("Type Your Message >>\n")
post_on_page(message)





