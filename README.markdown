# Quotes.txt #

## Keeping track of the stupid things you and your friends say online that no one (else) should read ##

Quotes.txt is a simple Django web app that allows you to post funny things you and your friends say in chat to a "quotes.txt" file (in reality, some kind of database) and review all of the funny things you've said over the years, but with zero context. It's inspired by the quotes.txt [@allanlawlor](http://twitter.com/allanlawlor) and I kept while I was working in government.

This is different from quote database sites like [bash.org](http://bash.org) in a few important ways:

  * Anyone can create a user account
  * There are "friend groups" to allow only you and your friends to post quotes
  * There is an HTTP API for posting your quotes in automated fashions

The last part is handy if you run a chat in Campfire or on IRC and want to create a bot that will automatically post a recent quote to the site. I encourage the bot to respond to `>> quotes.txt`, because that's kind of hilarious.

## Acknowledgments ##

Thanks to [Mozilla's playdoh](https://github.com/mozilla/playdoh) for some boilerplate ideas about handling local settings, app/lib/vendor folders, and package requirements.
