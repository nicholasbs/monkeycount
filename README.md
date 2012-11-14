#MonkeyCount

**MonkeyCount** is a simple script for exporting MailChimp subscriber activity
as a CSV file.

##Usage

Edit `settings.py` and set `API_KEY` (your MailChimp API key), `FROM_NAME` (the
from name of the campaigns you want stats for) and `MAX_CAMPAIGNS` (the maximum
number of campaigns you want stats for). Then run:

    $ python monkeycount.py > stats.csv

This will create a CSV file named `stats.csv` with data of the form:

    email,11/3/2012 23:51:52,10/27/2012 16:54:01
    nick@example.com,2,0
    kim@example.com,0,0
    dave@example.com,1,1

Rows list the activity count (clicks + opens) for each email address for
each campaign. In the above example, `nick@example.com` opened (or clicked) the campaign for 11/3 twice and had no activity for the 10/27 campaign.

## Requirements

[MailSnake](https://github.com/michaelhelmick/python-mailsnake)

##License

Copyright (c) 2012, Nicholas Bergson-Shilcock.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

  * Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
  * Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.
  * Neither the name of the <organization> nor the
    names of its contributors may be used to endorse or promote products
    derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
