
#functios to get the right path to save images of newsletter posts
def newletter_gram_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/post<year>/post<month>/<filename>
    return 'newsletter/{year}/{month}/{file}'.format(year=instance.post.year, month=instance.post.month, file=filename)
