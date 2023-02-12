
Description how to create an app you can find [here](https://developer.spotify.com/documentation/general/guides/authorization/app-settings/).   
Once you have got an app copy/paste to python script:  

```
CLIENT_ID = "<client_id>"
CLIENT_SECRET = "<client_secret>"
```

Last thing is the playlist link. Open your playlist, press **Share** and **Copy link to playlist** e.g.:  
`https://open.spotify.com/playlist/(...)`

```
$ python main.py | jq
{
  "items": [
    {
      "id": 1,
      "song": "<song>",
      "band": "<band>",
      "album": "<album>"
    },
    {
      "id": 2,
      "song": "<song>",
      "band": "<band>",
      "album": "<album>"
    }
  ]
}
```