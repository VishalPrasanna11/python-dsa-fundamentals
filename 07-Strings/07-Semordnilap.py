# Semordnilap
# A semordnilap is a word or a phrase that spells a different word when backwards ("semordnilap" is a semordnilap of "palindromes"). Here are some examples:
# EX 1: desserts & stressed 


def semordnilap(words):
    semordnilap_list = []
    for word in words:
        if word[::-1] in words:
            semordnilap_list.append([word, word[::-1]])
            words.remove(word)
            words.remove(word[::-1])
    return semordnilap_list

#Managing the edge case of "aaa" and "aaa" as semordnilap
def semordnilap(words):
    seen = set(words)
    semordnilap_list = []
    for word in words:
        reverse = word[::-1]
        if reverse in seen and reverse!= word:
            semordnilap_list.append([word, reverse])
            seen.remove(word)
            seen.remove(reverse)
    return semordnilap_list

print (semordnilap(["desserts", "stressed", "diaper", "repaid"])) #[['desserts', 'stressed'], ['diaper', 'repaid']]
print (semordnilap(["gateman", "nametag", "dog", "god"])) #[['gateman', 'nametag'], ['dog', 'god']]
print (semordnilap(["dog", "god", "desserts", "stressed"])) #[['dog', 'god'], ['desserts', 'stressed']]
print (semordnilap(["dog", "god", "desserts", "stressed", "diaper", "repaid"])) #[['dog', 'god'], ['desserts', 'stressed'], ['diaper', 'repaid']]