class RustfsChecker:
    @staticmethod
    def get_bucket_name(bucket_name: str) -> str:
        """生成符合 S3 规则的桶名

        转换规则：
        1. 下划线转连字符
        2. 转为小写
        3. 移除开头和结尾的非字母数字字符
        4. 确保不以 xn-- 开头
        5. 确保长度在 3-63 之间
        6. 处理连续点和连字符
        7. 确保不是 IP 地址格式

        参数:
            name (str): 原始名称

        返回:
            str: 符合 S3 规则的桶名
        """
