# Exercise Assets

Resources for Teachers and Students using the [BreatheCode Platform](https://breatheco.de).

Run this api on codespaces with `pipenv run start`

#### Important Note:
Some API methods are private and they will require the use of and access token in the URL query string like this:
> METHOD: /path/to/resource/?access_token={your_access_token}

The access token can be generated with this endpoint:


    POST: 
        /apis/events/token/generate

    PARAMS:
        - client_id (string): your client id
        - client_pass (string): your client password

If you don't have a client_id or client_pass send us an email to request it.

## Other Sample API's for Projects
- [TODO's API](/apis/fake/todos/)
- [Contact Management API](/apis/fake/contact/)
- [Sound API](/apis/fake/sound/)

<br/>
<br/>
<br/>
<br/>