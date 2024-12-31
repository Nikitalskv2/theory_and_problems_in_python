from collections import Counter

# 6. Сортировка слов по частоте

l = 'Nature is a masterpiece of beauty and complexity. From the vastness of the oceans to the towering heights of mountains, every element tells a story. Trees, with their intricate root systems and lush canopies, provide shelter and sustenance for countless species. Birds, with their vibrant feathers and melodious songs, add life and rhythm to the natural world. The changing seasons paint the landscape in a continuous cycle of renewal and transformation. Spring brings blooming flowers and fresh growth, while autumn showcases a breathtaking palette of colors. Humans, as part of this intricate web, have a responsibility to protect and preserve the wonders of nature for future generations.'


def used_count_word(s: str):
    n = s.split()
    c = Counter(n)
    return c.most_common(1)[0][0]

print(used_count_word(l))
