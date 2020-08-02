# ThatPersonDoesNotExist bulk downloader and classifier

This script downloads many images of AI generated people from thatpersondoesnotexist.com and then uses the py-agender library to classify and categorise them by gender and age

It moves them to directories categorised by gender and age group (customisable) and gives each file a filename in the format ```gender_age_randomstringtopreventduplicates.jpg```


## Installation

Install [py-agender](https://github.com/aristofun/py-agender) as per instructions on github repo

Install requests with ```pip3 install requests```

Install cv2 with ```pip3 install cv2```

## Default settings

The default settings for my purposes are as follows, but they are easily editable in the script:
* Download 100 images per run
* Classify images as child (under 20), young adult (under 30), adult (under 50) or older (50+)
* Ignore images of children

## Reliance and credit

This entirely relies on the work of thispersondoesnotexist.com and py-agender. You should ensure that your use of this tool is within what is permitted by them.
