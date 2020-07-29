
def tags_equal(tag1, tag2):
    return tag_format(tag1) == tag_format(tag2)

def tag_format(tag):
    new = tag[1:-1]
    print(new)
    #return name, *attribs = sorted(new.lower().split())

if __name__ == "__main__":
    print(tags_equal("<LABEL FOR=id_email for=id_username>", "<LABEL FOR=id_email>"))