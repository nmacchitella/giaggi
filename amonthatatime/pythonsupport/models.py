
#functios to get the right path to save images of newsletter posts
def newletter_gram_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/post<year>/post<month>/<filename>
    #return 'posts/{year}/{month}/{file}'.format(year=instance.post.year, month=instance.post.month,file=filename)
    return 'amonthatatime/images/posts/{year}/{month}/'.format(year=instance.post.year, month=instance.post.month)

#functios to get the right path to save images
def folder_upload(instance, filename):
    # file will be uploaded to MEDIA_ROOT/folder
    return '{folder}/{file}'.format(folder=instance.folder,file=filename)
