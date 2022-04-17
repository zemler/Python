#Import random lib
import random

def main():
    tab_length = random.randint(5,10)
    
    #Adding random values to tab:
    tab = []
    for x in range(tab_length):
        val = random.randint(1,100)
        tab.append(val)
    
    #Before Sort:
    print(f"Before Sort:\n{tab}")

    #Sort:
    for i in range(len(tab)):
        for j in range(len(tab)-1):
            if tab[j] > tab[j+1]:
                temp = tab[j]
                tab[j] = tab[j+1]
                tab[j+1] = temp

    #After Sort:
    print(f"After Sort:\n{tab}")


if __name__ == "__main__":
    main()
