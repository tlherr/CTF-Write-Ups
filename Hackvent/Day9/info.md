#Day 09: JSONion
### ... is not really an onion. Peel it and find the flag.

[tom@devbox Day9]$ file JSONion.zip 
JSONion.zip: Zip archive data, at least v2.0 to extract

Unzipping give us a file:

[tom@devbox Day9]$ file jsonion.json 
jsonion.json: ASCII text, with very long lines, with no line terminators

Get some pretty ugly JSON back (first few lines):

[
    {
        "op": "map",
        "mapTo": "[{\"op:gzi,cnteH4sIADSTXjNal\\/8d9wCByr30Qh+FYPxvqVUOWR7f56Zb21kuJGKmLEM=}]",
        "content": "/8ge+gugqP5+glgze:K2:KgugFis\"MMMMMMMMMonzJU2ps\\{S6NvsmOk]ZIn}h}oM\"p\"L\"RYXqFqB5ZCWM4]C4+fOvFXDXW{Y==jSsqhJThsX0VW[W6N6NhWbb[W6N6N3W6NUFiP6N6NxJhTbS:a{iW6Nn2m3D3XvKfz=JT3}UXb{xSbG4Vib5V36NTFXbYIQesiQjz6N6Nv6N93C\\[vV{f[y94PVb3EwL6N,q,GFA3V+4Yk5a43ejUyR


so we have a structure with op, mapTo, content, mapFrom

the slashes look like escape sequences, wondering what this is.

Could be some object dumped to json
