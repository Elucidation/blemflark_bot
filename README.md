# BlemflarkBot
[/u/BlemflarkBot](https://www.reddit.com/user/BlemflarkBot/) is a [Reddit](http://www.reddit.com) Bot whose sole purpose is to listen on [/r/rickandmorty](https://www.reddit.com/r/rickandmorty/) subreddit and provide currency conversions from Blemflarks to USD.

According to the season 3 premier of Rick and Morty, [1 Blemflark is worth $0](https://www.reddit.com/r/rickandmorty/comments/62ygal/the_value_of_the_blemflark/).

## Invoking BlemflarkBot

BlemflarkBot is usually running on a google cloud instance as a docker container.

If a comment has both a `<number> blemflark(s)` and one of the following: `how`, `what`, `?`, `!`, then the bot will generate a reply message that looks like something like [this](https://www.reddit.com/r/rickandmorty/comments/63dyo6/binging_with_babish_got_us_covered/dfvl7a7/):

===

> ...  how much is 42 blemflarks? ...

* 42 Blemflarks → **$0 USD**

---

<sup>[1 Blemflark = $0 USD](https://www.reddit.com/r/rickandmorty/comments/62ygal/the_value_of_the_blemflark/) | price not guaranteed | [`what is my purpose`](https://github.com/Elucidation/blemflark_bot 'I'll tell you, for money')</sub>

===

If you make a comment that satisfies those two requirements, and the bot is running, it will probably see and reply with the conversion within a couple minutes (10 minutes at worst).

Regex used: `p = re.compile('([^\n\.\,\r\d-]{0,30})(-?[\d|,]{0,300}\.{0,1}\d{1,300} bl?emfl?ark[\w]{0,80})([^\n\.\,\r\d-]{0,30})', re.IGNORECASE)`

This allows for variants on `blemflark` like blemflarks, BlemFarks!!!, blemflarkaronis, etc.

## Feedback/Comments

Several options from low priority to high:
* Send a PM to BlemflarkBot with comments.
* If there's an issue with a particular comment by BlemflarkBot, please either reply to that comment with the issue and downvote as needed, I'll be adding auto-deletion if a comment goes negative.
* For software issues/suggestions/feature requests, create a new issue on this Github.
