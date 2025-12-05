import gradio as gr

def bubble_sort_simulation(user_input):
    """
    This function takes a string of numbers, sorts them using Bubble Sort,
    and returns a log of the steps for visualization.
    """
    # Error Handling: Try to convert input to a list of integers
    try:
        # Split the string by commas and convert to integers
        nums = [int(x.strip()) for x in user_input.split(',')]
    except ValueError:
        return "Error: Please enter valid numbers separated by commas (e.g., 5, 1, 4, 2)."

    steps_log = [] # This will store the history of changes to show the user
    steps_log.append(f"Initial List: {nums}\n")
    
    n = len(nums)
    
    # --- Algorithm Implementation: Bubble Sort ---
    # Lloop through the list n times
    for i in range(n):
        swapped = False
        steps_log.append(f"--- Pass {i+1} ---")
        
        # Inner loop to compare side-by-side elements
        for j in range(0, n - i - 1):
            # COMPARE: Check if the left number is bigger than the right number
            if nums[j] > nums[j+1]:
                # SWAP: If yes, swap them
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
                steps_log.append(f"Swapped {nums[j+1]} and {nums[j]}: Current State -> {nums}")
            else:
                steps_log.append(f"No swap needed for {nums[j]} and {nums[j+1]}")

        # If no swaps occurred in this pass, the list is already sorted (Optimization)
        if not swapped:
            steps_log.append("No swaps made this pass. List is sorted!")
            break
            
    return "\n".join(steps_log)

# --- UI Setup using Gradio  ---
# Want a simple interface with one input box and one output box
with gr.Blocks() as demo:
    gr.Markdown("# Bubble Sort Visualizer")
    gr.Markdown("Enter numbers separated by commas to see how Bubble Sort swaps them in order.")
    
    with gr.Row():
        input_box = gr.Textbox(label="Input List (e.g., 5, 3, 8, 1)")
        output_box = gr.Textbox(label="Sorting Steps Log", lines=10)
    
    # Button to trigger the function
    sort_btn = gr.Button("Sort My List")
    sort_btn.click(fn=bubble_sort_simulation, inputs=input_box, outputs=output_box)

# Launch the app

demo.launch()
