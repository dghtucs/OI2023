好的，下面为您提供每个函数的使用示例：

1. `strlen()`：计算字符串的长度。
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Hello, world!";
    int length = strlen(str);
    printf("Length of the string is: %d\n", length);
    return 0;
}
```

2. `strcpy()`：将一个字符串复制到另一个字符串。
```c
#include <stdio.h>
#include <string.h>

int main() {
    char source[] = "Hello, world!";
    char destination[20];
    strcpy(destination, source);
    printf("Destination string: %s\n", destination);
    return 0;
}
```

3. `strncpy()`：将一个字符串的一部分复制到另一个字符串。
```c
#include <stdio.h>
#include <string.h>

int main() {
    char source[] = "Hello, world!";
    char destination[10];
    strncpy(destination, source, 5);
    destination[5] = '\0'; // Manually add null-terminator for the truncated string.
    printf("Destination string: %s\n", destination);
    return 0;
}
```

4. `strcat()`：将一个字符串连接到另一个字符串的末尾。
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[20] = "Hello, ";
    char str2[] = "world!";
    strcat(str1, str2);
    printf("Concatenated string: %s\n", str1);
    return 0;
}
```

5. `strncat()`：将一个字符串的一部分连接到另一个字符串的末尾。
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[20] = "Hello, ";
    char str2[] = "world!";
    strncat(str1, str2, 3);
    printf("Concatenated string: %s\n", str1);
    return 0;
}
```

6. `strcmp()`：比较两个字符串是否相等。
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "Hello";
    char str2[] = "Hello";
    if (strcmp(str1, str2) == 0) {
        printf("Strings are equal.\n");
    } else {
        printf("Strings are not equal.\n");
    }
    return 0;
}
```

7. `strncmp()`：比较两个字符串的一部分是否相等。
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "Hello";
    char str2[] = "Help";
    if (strncmp(str1, str2, 3) == 0) {
        printf("The first 3 characters are equal.\n");
    } else {
        printf("The first 3 characters are not equal.\n");
    }
    return 0;
}
```

8. `strchr()`：在一个字符串中查找指定字符的第一次出现。
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Hello, world!";
    char ch = 'o';
    char *ptr = strchr(str, ch);
    if (ptr != NULL) {
        printf("Character '%c' found at position: %ld\n", ch, ptr -

 str);
    } else {
        printf("Character '%c' not found.\n", ch);
    }
    return 0;
}
```

9. `strrchr()`：在一个字符串中查找指定字符的最后一次出现。
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Hello, world!";
    char ch = 'o';
    char *ptr = strrchr(str, ch);
    if (ptr != NULL) {
        printf("Last occurrence of character '%c' found at position: %ld\n", ch, ptr - str);
    } else {
        printf("Character '%c' not found.\n", ch);
    }
    return 0;
}
```

10. `strstr()`：在一个字符串中查找指定子串的第一次出现。
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Hello, world!";
    char substring[] = "world";
    char *ptr = strstr(str, substring);
    if (ptr != NULL) {
        printf("Substring '%s' found at position: %ld\n", substring, ptr - str);
    } else {
        printf("Substring '%s' not found.\n", substring);
    }
    return 0;
}
```

11. `strtok()`：将字符串分割为多个子串。
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Hello,world,how,are,you";
    char delimiters[] = ",";
    char *token = strtok(str, delimiters);
    while (token != NULL) {
        printf("Token: %s\n", token);
        token = strtok(NULL, delimiters);
    }
    return 0;
}
```

12. `memset()`：将一个字符串的每个字符设置为指定的值。
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[20] = "Hello, world!";
    memset(str, '*', 5);
    printf("Modified string: %s\n", str);
    return 0;
}
```

13. `memcpy()`：将一个字符串的一部分复制到另一个字符串。
```c
#include <stdio.h>
#include <string.h>

int main() {
    char source[] = "Hello, world!";
    char destination[20];
    memcpy(destination, source, 5);
    destination[5] = '\0'; // Manually add null-terminator for the truncated string.
    printf("Destination string: %s\n", destination);
    return 0;
}
```

14. `memmove()`：将一个字符串的一部分移动到另一个字符串。
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[20] = "Hello, world!";
    memmove(str + 7, str + 1, 5);
    printf("Modified string: %s\n", str);
    return 0;
}
```

15. `memcmp()`：比较两个字符串的内容是否相等。
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "Hello";
    char str2[] = "Help";
    int result = memcmp(str1, str2, 4);
    if (result == 0) {
        printf("The first 4 characters are equal.\n");
    } else if (result < 0) {
        printf("The first 4

 characters of str1 are less than str2.\n");
    } else {
        printf("The first 4 characters of str1 are greater than str2.\n");
    }
    return 0;
}
```

16. `strdup()`：复制一个字符串并返回一个指向新字符串的指针。
```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    char str[] = "Hello, world!";
    char *duplicate = strdup(str);
    printf("Duplicate string: %s\n", duplicate);
    free(duplicate); // Remember to free the dynamically allocated memory.
    return 0;
}
```

17. `strstr()`：在一个字符串中查找指定子串的第一次出现。
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Hello, world!";
    char substring[] = "world";
    char *ptr = strstr(str, substring);
    if (ptr != NULL) {
        printf("Substring '%s' found at position: %ld\n", substring, ptr - str);
    } else {
        printf("Substring '%s' not found.\n", substring);
    }
    return 0;
}
```

这些示例展示了每个函数的基本用法，您可以根据需要进行修改和扩展。