**applying what you know about lists to understand dictionaries**:

a `list` holds `elements` than can be accessed by the `index` **[an integer]** of that element using **bracket notation** like `list[index]`

a `dictionary` holds `values` that can be accessed by the `key` **[a string]** associated with that value using **bracket notation** like `dictionary["key"]`

a list uses an `index` to associate the position in memory where that `element` is stored. **a list is ordered** and this is why you can access its elements using an **integer** `index`

a dictionary uses a `key` to associate the position in memory where that `value` is stored. **a dictionary is unordered** and this is why you cannot access its values using an **integer** `index` and instead must use a **string** `key`[1]

accessing the element of a list DOES NOT USE QUOTES because, as we know, integer values do not have quotes which is what you use for the index.**

**accessing the value in a dictionary DOES USE QUOTES for the key because, as we know, strings do have quotes and the key is a string**

dictionaries and their counterparts in other languages are **absolutely ubiquitous** in programming. if you can understand how they function on a fundamental level you will be giving yourself a huge leg up in the coming sections

##### [1] - for the record there _are exceptions_ to this (you can have ints as keys for example). but the most common is for keys to be strings and it will help you get your footing before venturing off into less traditional key types
