# Async/Await from Scratch in Python

This repository contains a step-by-step implementation of the async/await functionality in Python from scratch. Each step is contained in a separate subfolder, allowing you to follow the progression and understand how async/await works under the hood.

## Steps

### Step0 - Basic Setup

The `Step0` subfolder contains a basic setup with a loop that runs a unit of work 100 times. This represents the situation we want to optimize using async/await.

### Step1 - Run Work in Parallel with a Thread Pool

In the `Step1` subfolder, we introduce the concept of running work in parallel using a thread pool. This step demonstrates how to distribute tasks across multiple threads to improve performance.

### Step2 - Tasks

The `Step2` subfolder focuses on implementing the concept of Tasks. Tasks are units of work that can be scheduled and executed asynchronously. This step adds the await part in that we wait for each task to finish before moving to the next.

### Step3 - Implement a RunAll() Function

In the `Step3` subfolder, we implement a `RunAll()` function. This function allows us to run multiple tasks concurrently and wait for all of them to complete. It showcases the power of async/await in handling concurrent operations.

### Step4 - Alternative Implementation with Coroutines

The `Step4` subfolder presents an alternative implementation of async/await using coroutines. Coroutines provide a way to write asynchronous code in a more sequential and readable manner. This step explores a different approach to achieving the same functionality.

### Step5 - Demo of Failure Points

In the `Step5` subfolder, we demonstrate potential failure points and edge cases when working with async/await. This step highlights thread locks and how they happen with coroutines vs threads.

## Getting Started

I just copy/paste the step into the main.py file and run that one. It's easy to see the changes from each step to the next.

## Requirements

- Python 3.x