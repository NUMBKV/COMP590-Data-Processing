function medianFiltering(signal, window_size, threshold) {
    /*
    Input: 
        signals: List of numbers 
        window_size: Integer, window size that calculate median from
        threshold: the ratio of difference between calculate median and given 
                    value that will be considered as an outlier
    
    Output: List of numbers that represent the index of outlier
    */  
    const result = signal.slice(0, Math.floor(window_size/2));
    for (let i = 0; i < signal.length-window_size+1; i++) {
        const temp = signal.slice(i, i + window_size);
        temp.sort((a, b) => a - b);
        let median;

        if(temp.length%2 != 0){
            let middleIndex = Math.floor(temp.length/2);
            median = temp[middleIndex];
        }else{
            let middleIndex = Math.floor(temp.length/2);
            median = temp[middleIndex] + temp[middleIndex + 1];
        }
        result.push(median);
    }
    
    for (let i = signal.length-Math.floor(window_size/2); i<signal.length; i++) {
        result.push(signal[i]);
    }


    const diff = []
    const outlier_index = []
    for (var i = 0; i<=result.length-1; i++)
        var val = Math.abs(result[i] - signal[i]) / (signal[i]+1);
        diff.push(val);
        if (val > threshold) {
            outlier_index.push(i)
        }
    return outlier_index

}

