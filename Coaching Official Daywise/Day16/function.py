def rp(s,p=',<>()*&^%$#@!'):
    for i in p:
        if i in s:
            s=s.replace(i,'')
print(s)
msz='hi ther<><:"" how a^&&&**&^^r#e #$you'
rp(msz)