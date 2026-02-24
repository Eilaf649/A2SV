for b in range(len(heights)):
            key=heights[b]
            j=b-1
            while(j>=0 and heights[j]<key):
                heights[j+1]= heights[j]
                j=j-1
            heights[j+1]= key
        for h in heights:
            arr.append(n[h])
