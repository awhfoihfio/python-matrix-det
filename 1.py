
"""Install sympy if not present, then import it."""
import sys
import subprocess

def ensure_sympy():
	try:
		import sympy  # noqa: F401
		return True
	except ImportError:
		subprocess.check_call([sys.executable, "-m", "pip", "install", "sympy"]) 
		try:
			import sympy  # noqa: F401
			return True
		except ImportError:
			return False

if __name__ == "__main__":
	ok = ensure_sympy()
	if ok:
		print("sympy is installed and importable")
	else:
		print("failed to install sympy", file=sys.stderr)
import sympy as sp

def calculate_symbolic_det():
    print("=== 符号矩阵行列式计算器 ===")
    
    # 1. 让用户输入矩阵的阶数
    try:
        n = int(input("请输入矩阵的阶数（例如 3 表示 3x3 矩阵）: "))
    except ValueError:
        print("请输入有效的整数！")
        return

    print(f"\n请输入一个 {n}x{n} 的矩阵。")
    print("元素可以是数字或字母（如 a, x, y），同一行的元素用【空格】隔开：")
    
    raw_rows = []
    for i in range(n):
        row_input = input(f"请输入第 {i+1} 行: ")
        # 将输入的字符串按空格切分
        row_elements = row_input.strip().split()
        
        if len(row_elements) != n:
            print(f"错误：这一行应该有 {n} 个元素，但你输入了 {len(row_elements)} 个。")
            return
        raw_rows.append(row_elements)
    
    # 2. 使用 sympy.sympify 将字符串转换成符号或数字
    try:
        sym_rows = [[sp.sympify(cell) for cell in row] for row in raw_rows]
        matrix = sp.Matrix(sym_rows)
    except Exception as e:
        print(f"解析输入时出错，请确保字母或公式书写正确。错误信息: {e}")
        return

    # 3. 计算行列式并化简
    print("\n--- 计算结果 ---")
    print("您的矩阵为：")
    sp.pprint(matrix)  # 漂亮地打印矩阵
    
    det = matrix.det()
    
    print("\n原始行列式结果：")
    print(det)
    
    print("\n化简后的结果（如果有化简空间）：")
    print(sp.simplify(det))

# 运行程序
if __name__ == "__main__":
    calculate_symbolic_det()
    