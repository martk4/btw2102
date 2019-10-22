authrs = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"}

#for author date in authors.items{}:        unsinnig 2 variablen, wennschon mit komma trennen, authrs anstatt authors
#    print("{2} died in {1}.".format(Date, authors)) 
#}
#output:

#Charles Dickens died in 1870.
#William Thackeray died in 1863.
#Anthony Trollope died in 1882.
#Gerard Manley Hopkins died in 1889.


for authors in authrs:
    print("{} died in {}.".format(authors,authrs[authors]))

print(authrs["Charles Dickens"])




