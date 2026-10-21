This is a debug message:
    If your numpy version >= 2.4.0, replace all
    np.in1d in scikit_roughsets/* by np.isin,
    or you will encounter AttributeError
    because np.in1d was removed in NumPy 2.4.0

    Since scikit_roughsets is a external libaray,
    you'd better fix it in .venv by your hand.