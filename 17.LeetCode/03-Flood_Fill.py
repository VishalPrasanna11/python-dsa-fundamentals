class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        source_value = image[sr][sc]
        if source_value == color:
            return image

        self.dfs(image, sr, sc, color, source_value)
        return image

    def dfs(self,image, sr, sc, color, source_value):


        if sr < 0 or sr > len(image)-1 or sc< 0 or sc > len(image[0])-1 or image[sr][sc] == color or image[sr][sc]!= source_value:
            return
        image[sr][sc] = color
        self.dfs(image,sr+1,sc,color,source_value)
        self.dfs(image,sr-1,sc,color,source_value)
        self.dfs(image,sr,sc+1,color,source_value)
        self.dfs(image,sr,sc-1,color,source_value)
