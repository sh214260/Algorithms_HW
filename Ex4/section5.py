def print_mermaid_tree():
    print("graph TD")
    
    # שורש
    print("t((10))")
    
    # בן שמאלי של השורש
    print("t --> tL((2))")
    
    # בן שמאלי של tL חסר - קודקוד ירק
    print("tL ~~~ tLL(( ))")
    print("style tLL fill:#fff,stroke-width:0px")
    
    # בן ימני של tL
    print("tL --> tLR((4))")
    
    # בן ימני של השורש
    print("t --> tR((16))")
    
    # בן שמאלי של tR
    print("tR --> tRL((15))")
    
    # בן ימני של tR
    print("tR --> tRR((17))")
    
    # בן שמאלי של tRR חסר - קודקוד ירק
    print("tRR ~~~ tRRL(( ))")
    print("style tRRL fill:#fff,stroke-width:0px")
    
    # בן ימני של tRR
    print("tRR --> tRRR((20))")

print_mermaid_tree()
